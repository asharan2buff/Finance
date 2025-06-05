from typing import Dict, Any

class ExplainerAgent:
    def process(self, state: Dict[str, Any]) -> Dict[str, Any]:
        # (Your “convert technical output into explanation” logic here.)
        return {
            # Note: graph.py’s _explainer_node expects a key called "explanation",
            # so make sure to return that if you want the final_result overwritten.
            "explanation": "Here is a user-friendly explanation of the results.",
            "confidence_score": 0.80,
            "metadata": {}
        }
