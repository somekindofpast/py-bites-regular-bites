from __future__ import annotations

import string

EOL_PUNCTUATION = ".!?"


class Document:
    lines: list[str]

    def __init__(self) -> None:
        # it is up to you how to implement this method
        # feel free to alter this method and its parameters to your liking
        self.lines = []

    def add_line(self, line: str, index: int = None) -> Document:
        """Add a new line to the document.

        Args:
            line (str): The line,
                expected to end with some kind of punctuation.
            index (int, optional): The place where to add the line into the document.
                If None, the line is added at the end. Defaults to None.

        Returns:
            Document: The changed document with the new line.
        """
        if index is not None and -1 < index < len(self.lines):
            self.lines.insert(index, line)
        else:
            self.lines.append(line)
        return self

    def swap_lines(self, index_one: int, index_two: int) -> Document:
        """Swap two lines.

        Args:
            index_one (int): The first line.
            index_two (int): The second line.

        Returns:
            Document: The changed document with the swapped lines.
        """
        if -1 < index_one < len(self.lines) and -1 < index_two < len(self.lines):
            line_copy = self.lines[index_one]
            self.lines[index_one] = self.lines[index_two]
            self.lines[index_two] = line_copy
        return self

    def merge_lines(self, indices: list) -> Document:
        """Merge several lines into a single line.

        If indices are not in a row, the merged line is added at the first index.

        Args:
            indices (list): The lines to be merged.

        Returns:
            Document: The changed document with the merged lines.
        """
        if not indices or len(indices) == 0 or not (-1 < indices[0] < len(self.lines)):
            return self

        append_index = indices.pop(0)

        text_to_add = ""
        for index in indices:
            if index and -1 < index < len(self.lines):
                text_to_add += ' ' + self.lines[index]
            else:
                return self

        self.lines[append_index] += text_to_add

        for index in sorted(indices, reverse=True):
            self.lines.pop(index)

        return self

    def add_punctuation(self, punctuation: str, index: int) -> Document:
        """Add punctuation to the end of a sentence.

        Overwrites existing punctuation.

        Args:
            punctuation (str): The punctuation. One of EOL_PUNCTUATION.
            index (int): The line to change.

        Returns:
            Document: The document with the changed line.
        """
        if not punctuation or punctuation == "" or punctuation not in EOL_PUNCTUATION:
            return self

        if index is None or not (-1 < index < len(self.lines)):
            return self

        if 0 < len(self.lines[index]) and self.lines[index][-1] in EOL_PUNCTUATION:
            self.lines[index] = self.lines[index][:-1]

        self.lines[index] += punctuation

        return self

    def word_count(self) -> int:
        """Return the total number of words in the document."""
        word_count = 0
        for line in self.lines:
            line = self._remove_punctuation(line)
            if line != "":
                word_count += len(line.split())
        return word_count

    @property
    def words(self) -> list:
        """Return a list of unique words, sorted and case insensitive."""
        unique_words = set()
        for line in self.lines:
            for word in line.split():
                word = self._remove_punctuation(word.lower()).strip(',')
                if word != "":
                    unique_words.add(word)
        return sorted(list(unique_words))

    def _remove_punctuation(self, line: str) -> str:
        """Remove punctuation from a line."""
        # you can use this function as helper method for
        # Document.word_count() and Document.words
        # or you can totally ignore it
        return line.strip(EOL_PUNCTUATION)

    def __len__(self):
        """Return the length of the document (i.e. line count)."""
        return len(self.lines)

    def __str__(self):
        """Return the content of the document as string."""
        res = ""
        for line in self.lines:
            res += line + '\n'
        return res.strip()


if __name__ == "__main__":
    # this part is only executed when you run the file and is ignored by the tests
    # you can use this section for debugging and testing
    d = (
        Document()
        .add_line("My second sentence.")
        .add_line("My first sentence.")
        .swap_lines(0, 1)
        .add_line("Introduction", 0)
        .add_punctuation("!", 0)
        .add_line("")
        .add_line("My second paragraph.")
        .merge_lines([1, 2])
    )

    print(d)
    print(len(d))
    print(d.word_count())
    print(d.words)

    print("-----------------------")
    d = (
        Document()
        .add_line("This is the tale of a dwarf.")
        .add_line("")
        .add_line("A dwarf you ask?")
        .add_line("Yes, a dwarf and not any dwarf, so you know!")
    )
    print(d)
    print(d.words)