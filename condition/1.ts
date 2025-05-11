import { assignRecipeToDate } from "../path/to/your/mutation";
import { createBadResponse, createOKResponse } from "../utils/responses";
import { HttpResponseCode } from "../constants/http";
import { getLatestRecipePlanDate } from "../helpers/getLatestRecipePlanDate";
import { MutationCtx } from "../types"; // adjust import based on your actual type location

jest.mock("../helpers/getLatestRecipePlanDate");

describe("assignRecipeToDate", () => {
  const mockCtx: MutationCtx = {
    db: {
      query: jest.fn(),
      insert: jest.fn(),
      patch: jest.fn(),
    },
  } as unknown as MutationCtx;

  const args = {
    groupId: "group-1",
    recipeId: "recipe-1",
    date: "2025-04-08",
  };

  beforeEach(() => {
    jest.clearAllMocks();
  });

  it("should return conflict if a groupPlan already exists", async () => {
    mockCtx.db.query.mockReturnValue({
      collect: () => Promise.resolve([{ id: "existing-plan" }]),
    });

    const result = await assignRecipeToDate.handler(mockCtx, args);

    expect(result).toEqual(createBadResponse(HttpResponseCode.Conflict));
  });

  it("should insert and patch correctly when no conflict", async () => {
    mockCtx.db.query.mockReturnValue({
      collect: () => Promise.resolve([]),
    });

    mockCtx.db.insert.mockResolvedValue(true);
    mockCtx.db.patch.mockResolvedValue(undefined);

    (getLatestRecipePlanDate as jest.Mock).mockResolvedValue({
      data: null,
    });

    const result = await assignRecipeToDate.handler(mockCtx, args);

    expect(mockCtx.db.insert).toHaveBeenCalledWith("groupPlans", {
      groupId: args.groupId,
      recipeId: args.recipeId,
      date: args.date,
    });

    expect(mockCtx.db.patch).toHaveBeenCalledWith(args.recipeId, {
      plannerDate: new Date(args.date).getTime(),
    });

    expect(result).toEqual(createOKResponse(true));
  });

  it("should patch using latestPreviousRecipePlanDate if available", async () => {
    mockCtx.db.query.mockReturnValue({
      collect: () => Promise.resolve([]),
    });

    mockCtx.db.insert.mockResolvedValue(true);

    const previousDate = "2025-03-15";

    (getLatestRecipePlanDate as jest.Mock).mockResolvedValue({
      data: previousDate,
    });

    await assignRecipeToDate.handler(mockCtx, args);

    expect(mockCtx.db.patch).toHaveBeenCalledWith(args.recipeId, {
      plannerDate: new Date(previousDate).getTime(),
    });
  });

  it("should return internal server error if insert fails", async () => {
    mockCtx.db.query.mockReturnValue({
      collect: () => Promise.resolve([]),
    });

    mockCtx.db.insert.mockResolvedValue(null);
    mockCtx.db.patch.mockResolvedValue(undefined);

    (getLatestRecipePlanDate as jest.Mock).mockResolvedValue({
      data: null,
    });

    const result = await assignRecipeToDate.handler(mockCtx, args);

    expect(result).toEqual(
      createBadResponse(HttpResponseCode.InternalServerError)
    );
  });
});
