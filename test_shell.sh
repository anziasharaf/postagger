#!/bin/bash

cp /home/user/Desktop/anzi/malayalam_nlplibrary/completed/pos_tagger/out.txt  /home/user/Desktop/anzi/malayalam_nlplibrary/completed/pos_tagger/POSTagging/Tnt
cd /home/user/Desktop/anzi/malayalam_nlplibrary/completed/pos_tagger/POSTagging/Tnt
./tnt tokenized_text out.txt > /home/user/Desktop/anzi/malayalam_nlplibrary/completed/pos_tagger/POSTagging/tagged_text.txt
