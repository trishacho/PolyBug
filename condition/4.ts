import { deleteStudent } from './deleteStudent';

interface Student {
  id: number;
  name: string;
}

// Mock the global showErrorModal function
global.showErrorModal = jest.fn();

describe('deleteStudent', () => {
  beforeEach(() => {
    jest.clearAllMocks();
  });

  it('should remove the student with the specified ID', () => {
    const students: Student[] = [
      { id: 1, name: 'Alice' },
      { id: 2, name: 'Bob' },
      { id: 3, name: 'Charlie' },
    ];

    deleteStudent(students, 2);

    expect(students).toEqual([
      { id: 1, name: 'Alice' },
      { id: 3, name: 'Charlie' },
    ]);
    expect(showErrorModal).not.toHaveBeenCalled();
  });

  it('should call showErrorModal if student is not found', () => {
    const students: Student[] = [
      { id: 1, name: 'Alice' },
      { id: 2, name: 'Bob' },
    ];

    deleteStudent(students, 999);

    expect(students.length).toBe(2); // no change
    expect(showErrorModal).toHaveBeenCalledWith("Error: no se ha encontrado el estudiante.");
  });
});
