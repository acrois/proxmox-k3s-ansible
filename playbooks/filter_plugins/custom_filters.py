import toml

def to_toml(data):
    return toml.dumps(data)

class FilterModule(object):
    def filters(self):
        return {
            'to_toml': to_toml,
        }