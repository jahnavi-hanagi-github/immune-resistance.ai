import random
import time

class Pathogen:
    def __init__(self, name, strength):
        self.name = name
        self.strength = strength
        self.alive = True

    def attack(self):
        print(f"[Pathogen] {self.name} is attacking with strength {self.strength}!")

class WhiteBloodCell:
    def __init__(self):
        self.power = random.randint(5, 15)

    def respond(self, pathogen):
        print(f"[WBC] Responding to {pathogen.name}...")
        if self.power >= pathogen.strength:
            pathogen.alive = False
            print(f"[WBC] {pathogen.name} destroyed!")
        else:
            print(f"[WBC] {pathogen.name} too strong! Need more help.")

class ImmuneSystem:
    def __init__(self):
        self.cells = [WhiteBloodCell() for _ in range(3)]
        self.memory_cells = []

    def detect_pathogen(self, pathogen):
        print(f"[ImmuneSystem] Pathogen detected: {pathogen.name}")
        if pathogen.name in self.memory_cells:
            print(f"[ImmuneSystem] Memory cells found! Fast response initiated.")
            pathogen.alive = False
            print(f"[ImmuneSystem] {pathogen.name} neutralized quickly!")
        else:
            self.fight(pathogen)

    def fight(self, pathogen):
        for cell in self.cells:
            if pathogen.alive:
                cell.respond(pathogen)
        if not pathogen.alive:
            self.memory_cells.append(pathogen.name)
            print(f"[ImmuneSystem] {pathogen.name} remembered for future defenses.")
        else:
            print(f"[ImmuneSystem] Infection persists. Need reinforcement!")

# Simulation
def run_simulation():
    pathogens = [
        Pathogen("Virus_A", random.randint(5, 15)),
        Pathogen("Bacteria_X", random.randint(5, 15)),
        Pathogen("Virus_A", random.randint(5, 15)),  # Repeated to test memory
    ]
    immune_system = ImmuneSystem()

    for pathogen in pathogens:
        print("\n--- New Threat Incoming ---")
        time.sleep(1)
        pathogen.attack()
        time.sleep(1)
        immune_system.detect_pathogen(pathogen)
        time.sleep(1)

run_simulation()

