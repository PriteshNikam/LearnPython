class Enemy:

    def __init__(self,enemy_type:str,enemy_power:int = 10,attack_damage:int = 1):
        self.enemy_type = enemy_type
        self.enemy_power = enemy_power
        self.attack_damage = attack_damage

    def enemy_talk(self):
        print("lets have a fight")

    def enemy_attack(self):
        print(f"{self.enemy_type} attacks with power {self.attack_damage}")

