from argparse import ArgumentParser


class Lexeme:
    pass


class Compiler:
    """
    Initial compiler for the Dream language.
    """
    def __init__(self):
        """
        Mostly implements the parser.
        """
        self.parser = ArgumentParser(description='initial compiler for Dream')
        self._init_parser()
        
    def _init_parser(self) -> ArgumentParser:
        """
        Actually implements the parser.
        """
        self.parser.add_argument('main', help='main file')

    def _read(self, file) -> str:
        """
        Reads from a file.
        """
        content = ''

        with open(file, "r") as f:
            content = f.read()

        return content
    
    def _write(self, file, content) -> None:
        """
        Writes to a file.
        """

        with open(file, "r") as f:
            f.write(content)

        return content
        
    def _compile(self, main: str) -> None:
        """
        Compiles a file.
        """
        raw = self._read(main)      # read raw file
        asm = self._parse(raw)      # parser

    def _parse(self, content: str) -> str:
        """
        Parses content based on lexigrahpical rules.
        """
        if ("int x = 2;" == content):
            print(content)
        
    def run(self) -> None:
        args = self.parser.parse_args()
        self._compile(args.main)


if __name__ == '__main__':
    compiler = Compiler()
    compiler.run()