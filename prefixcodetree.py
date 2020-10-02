class Node:
    def __init__(self):
        self.childs = [None, None]
        self.symbol = ''

class PrefixCodeTree:
    def __init__(self):
        self.root = Node()

    def insert(self, codeword, symbol):
        """A wrapper of insert_()"""
        self.insert_(self.root, codeword, symbol)

    def insert_(self, node, codeword, symbol):
        """
        Args:
            node: current node
            codeword: array of 0s and 1s
            symbol: string
        """
        if len(codeword) == 0:
            node.symbol = symbol        
        else:
            c = codeword[0]
            if node.childs[c] is None:
                node.childs[c] = Node()
            self.insert_(node.childs[c], codeword[1:], symbol)

    def traverse(self, node, data):
        """
        Args:
            node: current node
            data: array of 0s and 1s
        Returns:
            a string.
        """
        if len(data) == 0:
            return node.symbol

        if node.childs[data[0]] is None:
            return node.symbol + self.traverse(self.root, data)
        else: 
            return node.symbol + self.traverse(node.childs[data[0]], data[1:])

    def decode(self, encodedData, datalen):
        """
        Args:
            encodedData: array of bytes.
            datalen: len of the prefix that we care, the rest should be ignored.
        Returns:
            a string.
        """
        
        def getBits():
            """ Get a bitstring from encodedData, and trim to datalen """
            bits = []
            for i in range(len(encodedData)):
                for j in reversed(range(8)):
                    bit = ((1 << j) & encodedData[i]) 
                    if bit > 1: bit = 1
                    bits.append(bit)
                    
            bits = bits[:datalen]
            return bits

        assert datalen <= len(encodedData) * 8
        bits = getBits()
        return self.traverse(self.root, bits)
        
if __name__ == "__main__":
    a = b'\xd2\x9f\x20'
    codebook = {
        'x1': [0], 'x2': [1,0,0], 'x3': [1,0,1], 'x4': [1,1]
    }
    
    codeTree = PrefixCodeTree() # create a prefix code tree `codeTree`
    
    # Initialize codeTree with codebook
    for symbol in codebook:
        codeTree.insert(codebook[symbol], symbol)

    message = codeTree.decode(b'\xd2\x9f\x20', 21)
    print(message)
