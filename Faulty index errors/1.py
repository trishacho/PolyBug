import unittest
from your_module import Terminology, Concept, Mapping, Repository  # Adjust as per your actual module

class TestClosestMappings(unittest.TestCase):
    def setUp(self):
        self.repository = Repository()
        self.model_name = "sentence-transformers/all-mpnet-base-v2"

        self.terminology = Terminology(name="Terminology 1", id="1")
        self.concept = Concept(
            terminology=self.terminology,
            pref_label="Concept 1",
            concept_identifier="1"
        )
        self.mapping_1 = Mapping(
            concept=self.concept,
            text="Text 1",
            embedding=[0.1, 0.2, 0.3],
            sentence_embedder=self.model_name
        )
        self.mapping_2 = Mapping(
            concept=self.concept,
            text="Text 2",
            embedding=[0.2, 0.3, 0.4],
            sentence_embedder=self.model_name
        )
        self.mapping_3 = Mapping(
            concept=self.concept,
            text="Text 3",
            embedding=[1.2, 2.3, 3.4],
            sentence_embedder=self.model_name
        )

        self.repository.store_all([
            self.terminology,
            self.concept,
            self.mapping_1,
            self.mapping_2,
            self.mapping_3
        ])

    def test_get_closest_mappings(self):
        sample_embedding = [0.2, 0.4, 0.35]
        closest_mappings, distances = self.repository.get_closest_mappings(
            sample_embedding,
            limit=3
        )

        self.assertEqual(len(closest_mappings), 3)
        self.assertEqual(self.mapping_2.text, closest_mappings[0].text)

if __name__ == "__main__":
    unittest.main()
