vulnerability_name = "Calls in a loop"
vulnerability_description = """It seems that your contract has calls inside a loop. This might lead to Denial of Service attacks."""
vulnerability_recommendation = """Avoid looping calls, use Pull over Push strategy for external calls."""
more_info = ['https://fravoll.github.io/solidity-patterns/pull_over_push.html', 'https://coinsbench.com/solidity-tutorial-all-about-loops-ebe2fd332e59']