from review_gathering import Review

with Review() as r:
    r.land_first_page()
    r.select_book_to_search('Smart Start Stem, Grade 1')
    r.select_book()
    r.review_search()
    r.select_review()
