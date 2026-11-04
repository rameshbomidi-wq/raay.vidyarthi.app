#!/bin/bash
# usage: ocr.sh book lang
T=/tmp/claude-0/-home-claude/144695c1-f983-54b2-827a-850db5f3a853/scratchpad/tess
b=$1; l=$2; n=$(pdfinfo $b.pdf 2>/dev/null|awk '/Pages/{print $2}'); mkdir -p ocr_$b
seq 1 $n | xargs -P 3 -I{} bash -c "[ -s ocr_$b/{}.txt ] || { pdftoppm -f {} -l {} -r 200 -gray -singlefile $b.pdf ocr_$b/p{} && tesseract ocr_$b/p{}.pgm ocr_$b/{} -l $l --tessdata-dir $T >/dev/null 2>&1; rm -f ocr_$b/p{}.pgm; }"
echo done $b
