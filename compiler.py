import os
import re
from argparse import ArgumentParser
from pathlib import Path


class Compiler:
    """
    Initial compiler for the Dream language.
    """
    def __init__(self):
        self.parser = ArgumentParser(description='initial compiler for Dream')
        self._init_parser()
        
    def _init_parser(self) -> ArgumentParser:
        """
        Initializes the parser.
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
    
    def _get_root(self, root) -> str:
        """
        Gets the absolute path of the root dir.
        """

        cwd = os.getcwd()

        return str(Path(cwd, root))
    
    def _get_main(self, root) -> str:
        """
        Gets the main file.
        """

        return str(Path(root, 'src', 'main.dream'))
        
    def _compile(self, main: str) -> None:
        """
        Compiles a file.
        """
        raw = self._read(main)      # read raw file
        asm = self._parse(raw)      # parser

    def _parse(self, content: str) -> str:
        """
        Parses content based on lexigraphical rules.
        """
        # sanitize comments
        content = re.sub(r'#>\s*((?:.*\n)*?)\s*#>', '', content, flags=re.MULTILINE)
        content = re.sub(r'#=>\s*((?:.*\n)*?)\s*#=>', '', content, flags=re.MULTILINE)
        content = re.sub(r'#.*$', '', content, flags=re.MULTILINE)

        print(content)
        
    def run(self) -> None:
        args = self.parser.parse_args()
        root = self._get_root(args.main)
        main = self._get_main(root)

        self._compile(main)

        #self._compile(args.main)


if __name__ == '__main__':
    compiler = Compiler()
    compiler.run()