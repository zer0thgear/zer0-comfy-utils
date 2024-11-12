# zer0gear's ComfyUI Utils

A short collection of personal use nodes that I thought may be useful to others. No real coherence or theme here, just nodes that I wanted that I couldn't easily find.

## List Combine Node
Combines a list of strings into a single string, with each item separated by a specified separator. Intended for use with a tokenizer + prompt splitter, but could theoretically be used with anything that returns a list of strings.

Includes a Combine Last X Items variable to pre-combine the last X items in the list before adding the separator.

## Multiline String Node
Similar to a Note node, allows you to enter a multiline string but has an output widget to allow its contents to be passed to another node.