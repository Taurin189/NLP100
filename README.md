# NLP100
http://www.cl.ecei.tohoku.ac.jp/nlp100/

## Progress
### chapter1
|problem name|is solved?|
|:-----------|:------------:|
|00reverse_setring|○|
|01hry_off_string|○|
|02pi|○|
|03symbol_of_element|○|
|04reverse_setring|○|
|05n_gram|○|
|06collection|○|
|07template_text|○|
|08typoglycemia|○|

### chapter2
|problem name|is solved?|
|:-----------|:------------:|
|10count_line|○|
|11replace_tab_to_space|○|
|12divide_text|○|
|13merge_text|○|
|14display_n_line|○|
|15tail_file|○|
|16split_n_file|○|
|17unique_prefecture|○|
|18sort_3col|○|
|19count_same_words|○|

### chapter3
|problem name|is solved?|note|
|:-----------|:------------:|:------------:|
|20read_json|○||
|21extract_category_line|○||
|22extract_category_name|○||
|23extract_sections|○||
|24extract_medias|○||
|25extract_template|○||
|26delete_emphasize_markup|△|could not delete several markups|
|27delete_inner_link|△|could not delete several markups|
|28delete_mediawiki_markup|△|because of 26 and 27 problems|
|29extract_country_flag_url|-|not yet|

### chapter4
|problem name|is solved?|note|
|:-----------|:------------:|:------------:|
|create_mecab_file|○|Use Ochasen mode|
|30load_mecab_data|○||
|31extract_surface_verb|○||
|32extract_verb|○||
|33extract_strange_noun|○||
|34extract_word_combined_with_particles|○||
|35extract_serial_noun|△|it takes too much time|
|36extract_occurance_frequency|○||
|37extract_top_10_frequenct_word|○||
|38extract_frequenct_word|○||
|39extract_plot_zipf|○||

### chapter5
How to install mecab and Cabocha
https://qiita.com/musaprg/items/9a572ad5c4e28f79d2ae

エラー対応
https://qiita.com/tmf16/items/046cdcc5aaa36a3e76d7

グラフ表示のために必要なライブラリのインストール

    brew install graphviz
    pip install graphviz
    pip install pydotplus

|problem name|is solved?|note|
|:-----------|:------------:|:------------:|
|40make_morph_list|○||
|41make_chunk_list|○||
|42display_dst_and_srcs|○||
|43extract_verb_with_noun|○||
|44visualize_tree|○||
|45extract_verb_pattern|○||
|46extract_verb_with_subject|○||
|47extract_sa_verb_with_subject|||
|48|||
|49|||

### chapter6
in problem 52, I need to install stemming package

    pip install nltk

About problem 52, I need to understand "語幹".

["語幹"とは何かの参考ページ](https://english.chicken168.com/gokan/)

|problem name|is solved?|note|
|:-----------|:------------:|:------------:|
|50split_sentence|○||
|51extract_words|○||
|52stemming|||