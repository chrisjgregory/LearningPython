import random

p1_hp = 100
p2_hp = 100
turn = 1

print("⚔ 2 PLAYER BATTLE ARENA ⚔")
print("Moves: attack (safe), heavy (risky), heal")

while p1_hp > 0 and p2_hp > 0:
    print("\n----------------------")
    print("Player 1 HP:", p1_hp)
    print("Player 2 HP:", p2_hp)

    if turn == 1:
        move = input("Player 1 turn: ").lower()

        if move == "attack":
            damage = random.randint(10, 20)
            p2_hp -= damage
            print("💥 Player 1 dealt", damage)

        elif move == "heavy":
            if random.random() > 0.5:
                damage = random.randint(20, 35)
                p2_hp -= damage
                print("🔥 Heavy hit!", damage)
            else:
                print("❌ Heavy attack missed!")

        elif move == "heal":
            heal = random.randint(10, 20)
            p1_hp += heal
            print("💚 Player 1 healed", heal)

        else:
            print("Invalid move!")
            continue

        turn = 2

    else:
        move = input("Player 2 turn: ").lower()

        if move == "attack":
            damage = random.randint(10, 20)
            p1_hp -= damage
            print("💥 Player 2 dealt", damage)

        elif move == "heavy":
            if random.random() > 0.5:
                damage = random.randint(20, 35)
                p1_hp -= damage
                print("🔥 Heavy hit!", damage)
            else:
                print("❌ Heavy attack missed!")

        elif move == "heal":
            heal = random.randint(10, 20)
            p2_hp += heal
            print("💚 Player 2 healed", heal)

        else:
            print("Invalid move!")
            continue

        turn = 1

if p1_hp > 0:
    print("\n🏆 PLAYER 1 WINS!")
else:
    print("\n🏆 PLAYER 2 WINS!")
