class Tag:
    all_tags = []
    def __init__(self, obj, tag):
        self.obj = obj
        self.tag = tag # any value really

        # inserting into list
        Tag.all_tags.append(self)

    def get_tags(obj):
        return_tags = []
        for tag in Tag.all_tags:
            if tag.obj == obj:
                return_tags.append(tag)

        return return_tags

    def get_tag(obj, tag_val):
        for tag in Tag.get_tags(obj):
            if tag.tag == tag_val:
                return tag

    def has_tag(obj, tag_val):
        tag = Tag.get_tag(obj, tag_val)
        if tag != None:
            return True
        else:
            return False

    def add_tag(obj, tag_val):
        if Tag.has_tag(obj, tag_val) == False:
            Tag(obj, tag_val)

    def remove_tag(obj, tag_val):
        tag = Tag.get_tag(obj, tag_val)
        if tag:
            Tag.all_tags.remove(tag)
            del tag