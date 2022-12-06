vulnerability_name = "Use of assembly function"
vulnerability_description = """Assembly function in Solidity omits several security features of the language,
        therefore it is very error-prone."""
vulnerability_recommendation = """Avoid using the function, unless it is necessary, and you know how to use it."""
more_info = ['https://docs.soliditylang.org/en/v0.8.17/assembly.html?highlight=assembly', 'https://stefanoschaliasos.github.io/assets/papers/inline-oopsla22.pdf']