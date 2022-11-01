# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self):
        """ Initialize the trie """
        self.root = RouteTrieNode()

    def insert(self, path, handler):
        """
        Recursively add nodes and assign the handler to only the leaf 
        (deepest) node of this path

        Args:
            path(string): path to insert
            handler(string): handler
        """
        path_list = path.split("/")
        path_list = path.split("/")
        if len(path_list) >= 2 and path_list[-1] == "":
            path_list = path_list[:-1]
        current = self.root

        for string in path_list:
            if string in current.children:
                current = current.children[string]
            else:
                current = current.insert(string)
        current.handler = handler

    def find(self, path):
        """
        Navigate the Trie to find a match for this path

        Args:
            path(string): path to find 
        Return:
            handler for a match, or None for no match
        """
        path_list = path.split("/")
        if len(path_list) >= 2 and path_list[-1] == "":
            path_list = path_list[:-1]
        current = self.root
        for string in path_list:
            if string not in current.children:
                return None
            current = current.children[string]

        return current.handler


class RouteTrieNode:
    def __init__(self):
        """ Initialize the node with children and handler """
        self.children = {}
        self.handler = None

    def insert(self, string):
        """
        Insert into the node

        Args:
            string(string): string to insert 
        Return:
            inserted node
        """
        node = RouteTrieNode()
        self.children[string] = node
        return node

# The Router class will wrap the Trie and handle 
class Router:
    def __init__(self, root_handler, not_found_handler="404 handler"):
        """ initialize the router """
        self.trie = RouteTrie()
        self.root_handler = root_handler
        self.not_found_handler = not_found_handler
        self.trie.insert("/", self.root_handler)

    def add_handler(self, path, handler):
        """
        Add a handler for a path

        Args:
            path(string): path to lookup
            ha ndler(string): handler representation
        """
        self.trie.insert(path, handler)

    def lookup(self, path):
        """
        lookup path (by parts) and return the associated handler

        Args:
            path(string): path to lookup
        Return:
            string - handler representation
        """
        handler = self.trie.find(path)
        if not handler:
            return self.not_found_handler
        return handler

    def split_path(self, path):
        """
        split the path into a list of strings

        Args:
            path(string): path to split
        Return:
            list of strings
        """
        return path.split()


# Test case 1
router = Router("root handler", "not found handler")
router.add_handler("/home/about", "about handler")

assert router.lookup("/") == 'root handler'
assert router.lookup("/home") == 'not found handler'
assert router.lookup("/home/about/") == "about handler"

# Test case 2
router = Router("root handler")
router.add_handler("/api/v1/products", "product handler")

assert router.lookup("") == 'root handler'
assert router.lookup("/api/v1/products") == 'product handler'
assert router.lookup("/api/v1") == "404 handler"

# Test case 3
router = Router("index handler", "error handler")
router.add_handler("/courses/nd256", "course handler")
router.add_handler("/courses/nd256/review", "review handler")

assert router.lookup("//") == 'error handler'
assert router.lookup("/courses/nd256/review") == 'review handler'
