class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        dic = {
            'type': [],
            'color': [],
            'name': []
        }
        for item in items:
            dic['type'].append(item[0])
            dic['color'].append(item[1])
            dic['name'].append(item[2])
        
        return sum(1 for v in dic[ruleKey] if v == ruleValue)