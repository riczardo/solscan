vulnerability_name = "Hash collisions"
vulnerability_description = """Usage of abi.encodePacked() with different length arguments may lead to hash collision."""
vulnerability_recommendation = """You should not allow users to acces parameters used in abi.encodePacked(). Another solution is to simply use abi.encode() instead."""
more_info = ['https://swcregistry.io/docs/SWC-133?fbclid=IwAR0gJbHBugrG88rjbFahttGFNtN-RJFTeinvNbQik_WMY696NsKscVX83uc',
             'https://medium.com/swlh/new-smart-contract-weakness-hash-collisions-with-multiple-variable-length-arguments-dc7b9c84e493']
