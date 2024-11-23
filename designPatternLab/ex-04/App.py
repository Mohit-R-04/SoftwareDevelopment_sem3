from BinaryTree.BinarySearchTree import BinarySearchTree

class NewsApplication:
    def __init__(self):
        self.political_news_tree = BinarySearchTree()
        self.sports_news_tree = BinarySearchTree()

    def add_news(self, category, date, news):
        if category == 'Political':
            self.political_news_tree.insert((date, news))
        elif category == 'Sports':
            self.sports_news_tree.insert((date, news))
        else:
            raise ValueError("Category must be 'Political' or 'Sports'")

    def display_news_on_date(self, date, category):
        if category == 'Political':
            tree = self.political_news_tree
        elif category == 'Sports':
            tree = self.sports_news_tree
        else:
            raise ValueError("Category must be 'Political' or 'Sports'")

        news_list = tree.traverse('inorder')
        for news_date, news in news_list:
            if news_date == date:
                print(news)

    def display_news_between_dates(self, start_date, end_date, category):
        if category == 'Political':
            tree = self.political_news_tree
        elif category == 'Sports':
            tree = self.sports_news_tree
        else:
            raise ValueError("Category must be 'Political' or 'Sports'")

        news_list = tree.traverse('inorder')
        for news_date, news in news_list:
            if start_date <= news_date <= end_date:
                print(news)

# Example usage
if __name__ == "__main__":
    app = NewsApplication()
    app.add_news('Political', '2024-09-01', 'Political news 1')
    app.add_news('Sports', '2024-09-02', 'Sports news 1')
    app.add_news('Political', '2024-09-03', 'Political news 2')
    app.add_news('Sports', '2024-09-04', 'Sports news 2')

    print("News on 2024-09-01 (Political):")
    app.display_news_on_date('2024-09-01', 'Political')
    
    print("\nNews between 2024-09-01 and 2024-09-03 (Political):")
    app.display_news_between_dates('2024-09-01', '2024-09-03', 'Political')
