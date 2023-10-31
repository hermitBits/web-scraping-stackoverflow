# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from models.stack_overflow_item import StackOverflowNewest
from scrapy.exceptions import DropItem

from database.sqlite.db import session

from stack_overflow.spiders.newest import NewestSpider

class StackOverflowPipeline:
    def process_item(self, item, spider):
        
        if isinstance(spider, NewestSpider):
            adapter = ItemAdapter(item)

            new_item = StackOverflowNewest(
                url=adapter.get('url'), 
                description=adapter.get('description')
            )
            self.save_database(new_item)

        return item

    def save_database(self, new_item):
        try:
            session.add(new_item)
            session.commit()
        except Exception as e:
            session.rollback()
            raise DropItem(f"Erro ao adicionar item ao banco de dados: {e}")
