let gold, currentWeaponIndex, weapons, inventory, goldText, text;

beforeEach(() => {
  // Reset values before each test
  gold = 100;
  currentWeaponIndex = 0;
  weapons = [
    { name: "Stick" },
    { name: "Dagger" },
    { name: "Sword" }
  ];
  inventory = [];

  goldText = { innerText: "" };
  text = { innerText: "" };

  global.gold = gold;
  global.currentWeaponIndex = currentWeaponIndex;
  global.weapons = weapons;
  global.inventory = inventory;
  global.goldText = goldText;
  global.text = text;
});

function myWeapon() {
  if (currentWeaponIndex < weapons.length - 1) {
    if (gold >= 30) {
      gold -= 30;
      currentWeaponIndex++;
      goldText.innerText = gold;
      let newWeapon = weapons[currentWeaponIndex].name;
      inventory.push(newWeapon);
      text.innerText = "You now have a " + newWeapon + ".";
      text.innerText += " In your inventory you have: " + inventory.join(", ");
    } else {
      text.innerText = "You do not have enough gold to buy a weapon.";
    }
  } else {
    text.innerText = "You already have the best weapon!";
  }
}

test("successfully buys a new weapon", () => {
  myWeapon();
  expect(currentWeaponIndex).toBe(1);
  expect(gold).toBe(70);
  expect(goldText.innerText).toBe(70);
  expect(inventory).toContain("Dagger");
  expect(text.innerText).toContain("You now have a Dagger.");
  expect(text.innerText).toContain("In your inventory you have: Dagger");
});

test("fails to buy weapon due to low gold", () => {
  gold = 10;
  global.gold = gold;

  myWeapon();
  expect(currentWeaponIndex).toBe(0);
  expect(gold).toBe(10);
  expect(inventory.length).toBe(0);
  expect(text.innerText).toBe("You do not have enough gold to buy a weapon.");
});

test("fails to buy weapon because already has the best", () => {
  currentWeaponIndex = weapons.length - 1;
  global.currentWeaponIndex = currentWeaponIndex;

  myWeapon();
  expect(currentWeaponIndex).toBe(2);
  expect(text.innerText).toBe("You already have the best weapon!");
});
