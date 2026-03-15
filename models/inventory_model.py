```json
{
    "models/inventory_model.py": {
        "content": "
import logging
from typing import Dict, List
from adept.ai import StateGraph
from deepeval import EvaluationMetric
from langfuse import LangGraph

logging.basicConfig(level=logging.INFO)

class InventoryModel:
    def __init__(self, non_stationary_drift_index: float, stochastic_regime_switch: bool):
        """
        Initialize the inventory model.

        Args:
        - non_stationary_drift_index (float): The index of non-stationary drift in the inventory data.
        - stochastic_regime_switch (bool): Whether to use stochastic regime switch in the model.

        Returns:
        - None
        """
        self.non_stationary_drift_index = non_stationary_drift_index
        self.stochastic_regime_switch = stochastic_regime_switch
        self.state_graph = StateGraph()
        self.lang_graph = LangGraph()

    def optimize_inventory(self, inventory_levels: List[float]) -> Dict[str, float]:
        """
        Optimize the inventory levels using the state graph and lang graph.

        Args:
        - inventory_levels (List[float]): The current inventory levels.

        Returns:
        - Dict[str, float]: The optimized inventory levels.

        Raises:
        - Exception: If the optimization fails.
        """
        try:
            logging.info('Optimizing inventory levels...')
            self.state_graph.optimize(inventory_levels)
            self.lang_graph.optimize(inventory_levels)
            optimized_levels = self.state_graph.get_optimized_levels()
            logging.info('Optimization complete.')
            return optimized_levels
        except Exception as e:
            logging.error(f'Optimization failed: {e}')
            raise

    def evaluate_inventory(self, inventory_levels: List[float]) -> EvaluationMetric:
        """
        Evaluate the inventory levels using the evaluation metric.

        Args:
        - inventory_levels (List[float]): The current inventory levels.

        Returns:
        - EvaluationMetric: The evaluation metric for the inventory levels.

        Raises:
        - Exception: If the evaluation fails.
        """
        try:
            logging.info('Evaluating inventory levels...')
            evaluation_metric = EvaluationMetric(inventory_levels)
            evaluation_metric.evaluate()
            logging.info('Evaluation complete.')
            return evaluation_metric
        except Exception as e:
            logging.error(f'Evaluation failed: {e}')
            raise

if __name__ == '__main__':
    # Simulate the 'Rocket Science' problem
    inventory_model = InventoryModel(non_stationary_drift_index=0.5, stochastic_regime_switch=True)
    inventory_levels = [100.0, 200.0, 300.0]
    optimized_levels = inventory_model.optimize_inventory(inventory_levels)
    evaluation_metric = inventory_model.evaluate_inventory(optimized_levels)
    logging.info(f'Optimized inventory levels: {optimized_levels}')
    logging.info(f'Evaluation metric: {evaluation_metric}')
",
        "commit_message": "feat: implement specialized inventory_model logic"
    }
}
```