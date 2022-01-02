
class Table:
    def __init__(self, *fields):
        self.data = {}
        self.cursor = 0
        self.fields = fields

    def insert(self, **params):
        # Requirements:
        #   - Add a record entry to the self.data dictionary

        #   - BUT ::::
        #   - Validate that params is a (1) dictionary (2) non-empty (3) Keys are in self.fields list
        #   - Ensure to generate a record id for the new record using the cursor attribute. Note: ids must always start from 1
        #   - Ensure to use generated id as key for insert and also inject into the actual record to be inserted with the key => _id
        #   - Manually or allow python to raise appropriate exceptions when there are errors
        #   - Return a dictionary representing the record that has just been successfully inserted

        # Remove the pass statement below and add your implementation there ...
        if len(params) == 0:
            raise ValueError("No Entry!")
        
        if not isinstance(params, dict):
            raise TypeError("Enter a dictionary")
        
        for item in params:
            if item not in self.fields:
                raise ValueError("Invalid Input Format")
        
        self.cursor += 1
        given_id = self.cursor
        params["_id"] =  given_id
        self.data[given_id] = params
        
        return self.data[given_id]
        
        

    def select(self, **conditions):
        # Requirements:
        #   - Filter and return records that has values matching those in the conditions argument
        #   - BUT ::::
        #   - Validate that conditions is a (1) dictionary (2) non-empty (3) Keys are in self.fields list
        #   - Manually or allow python to raise appropriate exceptions when there are errors
        #   - Return a list of dictionaries representing records that matched entires in the conditions argument

        # Remove the pass statement below and add your implementation there ...
        if len(conditions) == 0:
                raise ValueError("No Entry")
        
        if not isinstance(conditions, dict):
            raise TypeError("Enter a dictionary")
        
        for keys in conditions:
            if keys not in self.fields:
                raise ValueError("Invalid Input Format")
        
        arr = []
        for item in self.data.values():
            for key, value in conditions.items():
                if item[key] == value:
                    arr.append(item)
                    
        return arr
            
        
