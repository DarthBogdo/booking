from selenium import webdriver
import constants as const
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class Review(webdriver.Chrome):
    def __init__(self):
        super(Review, self).__init__()
        self.implicitly_wait(15)
        self.maximize_window()

    def land_first_page(self):
        self.get(const.BASE_URL)
        time.sleep(7)

    def select_book_to_search(self, book):
        search_field = self.find_element(By.ID, 'twotabsearchtextbox')
        search_field.clear()
        search_field.send_keys(book)
        time.sleep(0.5)
        self.find_element(By.ID, 'nav-search-submit-button').click()

    def select_book(self):
        time.sleep(2)
        selection_element = self.find_element(By.XPATH, '//*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div[2]/div/div/div/div/div/div[2]/div/div/div[1]/h2/a/span')
        selection_element.click()

    def review_search(self):
        self.execute_script("window.scrollTo(0, 300)")
        time.sleep(1)
        self.execute_script("window.scrollTo(0, 540)")
        time.sleep(1)
        self.execute_script("window.scrollTo(0, 540)")
        time.sleep(1)
        confirmation_1 = WebDriverWait(self, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="a-autoid-18"]')))
        recent = self.find_element(By.XPATH, '//*[@id="a-autoid-18"]')
        recent.click()
        time.sleep(2)
        if self.current_url == 'https://www.amazon.com/ap/signin?openid.return_to=https%3A%2F%2Fwww.amazon.com%2Fdp%2F1629385417%2Fref%3Dcm_cr_dp_d_vote_lft%3Fie%3DUTF8%26csrfT%3DhNTsvHMpo%252BvgIbSpuORohcgJmaGhGKHbu%252BVlyZUTBxshAAAAAGQoT8YAAAAB%26reviewId%3DR39N4Y4XXG22LH%23R39N4Y4XXG22LH&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&marketPlaceId=ATVPDKIKX0DER&language=en&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0':
            self.back()
        confirmation_2 = WebDriverWait(self, 10).until(
            EC.presence_of_element_located((By.ID, 'cm-cr-sort-dropdown_1')))
        print('problem')
        recent1 = self.find_element(By.ID, 'cm-cr-sort-dropdown_1')
        recent1.click()
        time.sleep(5)

    def select_review(self):
        # confirmation_3 = WebDriverWait(self, 10).until(
        #     EC.presence_of_element_located((By.ID, 'cm-cr-dp-review-list')))
        # review1 = self.find_element(By.XPATH, "//div[@data-hook='review']")
        # review1_text = review1.find_element(By.XPATH, "//div[@data-hook='review-collapsed']").text
        # print(review1_text)
        confirmation_3 = WebDriverWait(self, 10).until(
            EC.presence_of_element_located((By.ID, 'cm-cr-dp-review-list')))
        reviews = []
        for i in [1, 2, 3, 4, 5]:
            review = self.find_elements(By.XPATH, 'html/body/div[1]/div[2]/div[4]/div[35]/div/div/div[2]/div/div[2]/span[2]/div/div/div[3]/div[3]/div/div[{}].'.format(i))
            review_text = review.find_element(By.XPATH, "//div[@data-hook='review-collapsed']").text
            reviews.append(review_text)
        print(reviews)



