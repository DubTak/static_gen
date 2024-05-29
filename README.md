# static_gen
static site generator project

## Change Log
4d8fb76 (HEAD -> main, origin/main, origin/HEAD) Update gencontent.py with generate_pages_recursive and adjusted main.py accordingly, Add new pages via content/majesty, Finish project
22f337e Add gencontent.py and template.html and content/index.md, Update main.py and main.sh to generate site
c81aab6 Add copystatic.py and static/, Delete public/ and append it to .gitignore
7598ba6 Create markdown_to_html function in markdown_blocks, Update various to implement
903eb01 Update markdown_blocks with block_to_block_types, Update test_markdown_blocks with tests
db79b3a Fix indents in markdown_blocks
a82c851 Add markdown_block.py and test_markdown_block.py
d6eadeb Update inline_markdown with text_to_textnode, Update various to integrate
b3fbaeb Update inline_markdown with split_nodes_image and split_nodes_link, Update test_inline_markdown with tests for new funcs
d968d13 Update inline_markdown and test_inline_markdown with extract_markdown_images and extract_markdown_links
dcecc71 Add inline_markdown.py and test_inline_markdown.py and Update textnode.py with text_node_to_html_node()
a4d83c1 Update htmlnode.py with ParentNode class and Update various to integrate
a73e03f Update htmlnode.py with LeafNode class and Update various to integrate
5a28263 Add htmlnode.py and test_htmlnode.py and Update various in src/
0a63122 Add test.sh and test_textnode.py and Update textnode.py
80435ac Add main.py and main.sh and textnode.py and gitignore
4e4368a Add public/styles.css and Update public/index.html
63e0e07 Add server.py and public/index.html
a9d85af Initial commit