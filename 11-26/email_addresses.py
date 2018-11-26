class Solution:
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        
        unique = set()
        
        for email in emails:
            
            local, domain = email.split('@')
            
            # Get rid of the periods in local
            local = local.replace('.', '')
            # Get rid of everything after the first +
            plus_index = local.find('+')
            
            if plus_index != -1:
                local = local[:plus_index]
            
            unique.add('@'.join((local, domain)))
            
        return len(unique)
        
