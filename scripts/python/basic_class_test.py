import unittest
import graph_class as gc


class TestGraphMethods(unittest.TestCase):
    """
    Test basic graph functionality.
    """
    def setUp(self):
        self.test_graph = gc.Graph()
        self.test_graph.connect('A', 'B')
        self.test_graph.connect('B', 'C')
        self.test_graph.connect('D', 'F')

    def test_type_test(self):
        """
        Makes sure all the types, and the graph structure is in order.
        """
        self.assertIsInstance(self.test_graph.get_nodes(), dict)
        self.assertEqual(set(self.test_graph.get_nodes().keys()), {'A', 'B', 'C', 'D', 'F'})
        for name in self.test_graph.get_nodes():
            self.assertIsInstance(self.test_graph.get_neighbours(name), dict)
        self.assertIn('B', self.test_graph.get_neighbours('A'))
        self.assertIn('A', self.test_graph.get_neighbours('B'))

    def test_create_test(self):
        """
        Makes sure it is possible to create a node in the graph.
        """
        self.test_graph.create_node('E', {'D': 1})
        self.assertIn('E', self.test_graph.get_nodes())
        self.assertIn('D', self.test_graph.get_neighbours('E'))
        self.assertIn('E', self.test_graph.get_neighbours('D'))

    def test_connect_nodes(self):
        """
        Makes sure it is possible to create a node via connect.
        """
        self.test_graph.connect('NEW', 'A')
        self.assertIn('NEW', self.test_graph.get_nodes())
        self.assertIn('NEW', self.test_graph.get_neighbours('A'))

    def test_remove(self):
        """
        Makes sure gc.remove() works properly.
        """
        self.test_graph.remove('A')
        self.assertNotIn('A', self.test_graph.get_nodes())
        self.assertNotIn('A', self.test_graph.get_neighbours('B'))

    def test_get_sub_graph(self):
        """
        Tests the method get_sub_graph.
        """
        deq, disc = self.test_graph.get_sub_graph('A', {'A':1, 'B':1,'C':1})
        self.assertEqual(set(deq), {'A', 'B', 'C'})
        self.assertEqual(disc, {})

    def test_csg_ify(self):
        """
        Tests the method csg_ify
        """
        lines = list(self.test_graph.csg_ify())
        for line in lines:
            line = set(line.split("\t"))
            self.assertTrue((line == {'A', 'B', 'C'}) or (line == {'D', 'F'}))
        self.assertTrue(lines[0] != lines[1] and len(lines) == 2)

    def test_parser(self):
        """
        Tests the class method parser.
        """
        parsed = gc.Graph.parse("../../resources/test_input.txt")
        self.assertEqual(parsed.get_nodes(), self.test_graph.get_nodes())

if __name__ == '__main__':
    unittest.main()
