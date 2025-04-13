class ImmuneSystem:
    def __init__(self, species):
        self.species = species

    def respond_to_disease(self, disease):
        print(f"\n[{self.species}] Encountered Disease: {disease.name} ({disease.category})")
        print(f"[{self.species}] Symptoms: {', '.join(disease.symptoms)}")
        self.innate_response(disease)
        self.adaptive_response(disease)

    def innate_response(self, disease):
        print(f"[{self.species}] Innate immune response activated: Fever, Inflammation, Macrophages")

    def adaptive_response(self, disease):
        if disease.category in ["Viral", "Bacterial"]:
            print(f"[{self.species}] Adaptive immune response: Antibodies produced, T-Cells activated")
        elif disease.category == "Parasitic":
            print(f"[{self.species}] Adaptive immune response: Eosinophils and IgE activated")
        elif disease.category == "Fungal":
            print(f"[{self.species}] Adaptive immune response: Neutrophils and Th17 cells activated")
        else:
            print(f"[{self.species}] Adaptive immune response: General immune cells activated")
        print(f"[{self.species}] Memory cells formed for {disease.name}")

class Disease:
    def __init__(self, name, category, symptoms):
        self.name = name
        self.category = category
        self.symptoms = symptoms

def load_diseases():
    return [
        Disease("COVID-19", "Viral", ["Cough", "Fever", "Fatigue"]),
        Disease("Tuberculosis", "Bacterial", ["Cough", "Weight loss", "Night sweats"]),
        Disease("Malaria", "Parasitic", ["Fever", "Chills", "Headache"]),
        Disease("Candidiasis", "Fungal", ["Itching", "Discharge", "Redness"]),
        Disease("Ebola", "Viral", ["Fever", "Bleeding", "Vomiting"]),
        Disease("Cholera", "Bacterial", ["Diarrhea", "Dehydration"]),
        Disease("Toxoplasmosis", "Parasitic", ["Flu-like symptoms", "Muscle aches"]),
        Disease("Aspergillosis", "Fungal", ["Coughing", "Shortness of breath"]),
        Disease("Dengue", "viral", ["fever","chills","dysentry"]),
        Disease("Bronchities","flu" ["breathlessness","puffing of bronchioles","coughing"]),
    ]

def main():
    human = ImmuneSystem("Human")
    animal = ImmuneSystem("Animal")

    diseases = load_diseases()

    for disease in diseases:
        human.respond_to_disease(disease)
        animal.respond_to_disease(disease)

if __name__ == "__main__":
    main()


