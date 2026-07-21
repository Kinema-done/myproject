# === Stage 18: Добавь поддержку тегов и операции добавления/удаления тегов ===
# Project: ExpenseSplit
class Tag:
    def __init__(self, name):
        self.name = name.lower()
    
    @property
    def is_valid(self):
        return len(self.name) > 0
    
    def __eq__(self, other):
        if isinstance(other, Tag):
            return self.name == other.name
        return False
    
    def __hash__(self):
        return hash(self.name)


class ExpenseSplit:
    def __init__(self, name="", members=None, tags=None):
        self.name = name
        self.members = {} if members is None else {m.name.lower(): m for m in members}
        self.tags = set(tags) if isinstance(tags, (list, tuple)) else set()
        self.history = []

    def add_member(self, member):
        self.members[member.name.lower()] = member
    
    def remove_member(self, name):
        self.members.pop(name.lower(), None)
    
    def get_balance(self):
        balance_map = {m: 0 for m in self.members}
        for expense in self.history:
            if isinstance(expense, Expense):
                for member_name, amount in zip(expense.payors, expense.amounts):
                    balance_map[member_name.lower()] -= amount
                for member_name, amount in zip(expense.split_members, expense.splits):
                    balance_map[member_name.lower()] += amount
        return BalanceReport(balance_map)

    def get_history(self):
        return [h for h in self.history if isinstance(h, Expense)]


class TaggedExpense(Expense):
    def __init__(self, payors=None, amounts=None, split_members=None, splits=None, tags=None, date=None):
        super().__init__(payors=payors, amounts=amounts, split_members=split_members, splits=splits, date=date)
        self.tags = set(tags) if isinstance(tags, (list, tuple)) else set()

    def add_tag(self, tag_name):
        tag = Tag(tag_name)
        if not tag.is_valid:
            raise ValueError(f"Invalid tag name: {tag_name}")
        self.tags.add(tag)
    
    def remove_tag(self, tag_name):
        tag = Tag(tag_name)
        if not tag.is_valid:
            raise ValueError(f"Invalid tag name: {tag_name}")
        self.tags.discard(tag)
