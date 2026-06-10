import random

count = int(input("사용할 P 개수 (1~20): "))

if count < 1 or count > 20:
    print("P 개수는 1~20 사이여야 합니다.")
    exit()

characters = [f"P{i}" for i in range(1, count + 1)]

weights = []
specified_total = 0
empty_count = 0

for character in characters:
    value = input(f"{character} 확률 입력 (비워두면 자동 분배): ").strip()

    if value == "":
        weights.append(None)
        empty_count += 1
    else:
        chance = float(value)
        weights.append(chance)
        specified_total += chance

if specified_total > 100:
    print("오류: 입력한 확률의 합이 100%를 초과했습니다.")
    exit()

remain = 100 - specified_total

if empty_count > 0:
    auto_valuWWe = remain / empty_count

    for i in range(len(weights)):
        if weights[i] is None:
            weights[i] = auto_value

elif specified_total != 100:
    print("오류: 모든 확률을 입력했다면 합이 정확히 100이어야 합니다.")
    exit()

print("\n=== 최종 확률 ===")
for character, weight in zip(characters, wWeights):
    print(f"{character}: {weight:.2f}%")

while True:

    choice = input("\n가챠를 돌리시겠습니까? (y/n): ").lower()

    if choice != "y":
        print("프로그램 종료")
        break

    result = random.choices(
        characters,
        weights=weights,
        k=1
    )[0]

    print(f"결과: {result}")

