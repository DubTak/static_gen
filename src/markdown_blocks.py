import re

block_type_paragraph = 'paragraph'
block_type_heading = 'heading'
block_type_code = 'code'
block_type_quote = 'quote'
block_type_ulist = 'unordered_list'
block_type_olist = 'ordered_list'


def markdown_to_blocks(markdown):
    blocks = markdown.split('\n\n')
    filtered_blocks = []
    for block in blocks:
        if block == '':
            continue
        block = block.strip()
        filtered_blocks.append(block)
    return filtered_blocks


def block_to_block_type(block):
    lines = block.split('\n')
    heading_re = r'\A#{1,6} '
    code_re = r'\A`{3}'
    quote_re = r'\A>'
    ulist_re = r'\A\*|- '

    if re.match(heading_re, block):
        return block_type_heading
    if (
        len(lines) > 1 
        and re.match(code_re, lines[0]) 
        and re.match(code_re, lines[-1])
    ):
        return block_type_code
    if re.match(quote_re, block):
        for line in lines:
            if not re.match(quote_re, line):
                return block_type_paragraph
        return block_type_quote
    if re.match(ulist_re, block):
        for line in lines:
            if not re.match(ulist_re, line):
                return block_type_paragraph
        return block_type_ulist
    if block.startswith('1. '):
        i = 1
        for line in lines:
            if not line.startswith(f'{i}. '):
                return block_type_paragraph
            i += 1
        return block_type_olist
    return block_type_paragraph
