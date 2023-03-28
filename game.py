import random

# 공용 틀


class Character:
    def __init__(self, name, hp, power):
        self.name = name  # 이름
        self.max_hp = hp  # 최대 체력
        self.current_hp = hp  # 현재 체력
        self.power = power  # 물리 공격력

    def attack(self, target):
        print(f"{self.name}의 attack!")
        pass

    def show_status(self):
        # 상태 출력
        print(f"{self.name}의 상태: HP {self.hp}/{self.max_hp}
              MP {self.mp}/{self.max_mp} ")
        pass

# 플레이어


class Player(Character):
    def __init__(self, name, hp, mp, power, magic_power):
        super().__init__(name, hp, power)
        self.max_mp = mp  # 최대 마나
        self.current_mp = mp  # 현재 마나
        self.magic_power = magic_power

    def magic_attack(self, target):
        print(f"{self.name}의 magic_attack!")
    pass

# 몬스터


class Monster(Character):
    pass

    # 플레이어 이름 입력
    player_name = input("이름을 입력해주세요 > ")


# 플레이어 생성
player = Player(name=player_name)
monster = Monster("거대 바퀴벌레", 100, 15)

while True:
    player.show_status()
    monster.show_status()
    action = input(1: 일반공격   2: 마법공격)

    if action == "1":
        player.attack("target")
    elif action == "2":
        player.magic_attack("target")

    # 튜터님은 여기서 3번에 exit도 추가하심
    # elif action == "exit":
    # sys.exit()

    # 여기서 continue를 사용하지 않으면 계속
    else:
        print("정확한 값을 입력해 주세요.")
    continue

monster.attack("target")
