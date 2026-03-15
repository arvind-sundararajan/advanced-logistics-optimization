```json
{
    "utils/constants.py": {
        "content": "
import logging
from typing import Dict, List, Tuple
from langfuse import StateGraph
from deepeval import EvaluationMetrics

# Initialize logger
logger = logging.getLogger(__name__)

class Constants:
    """
    Class containing constants for the Autonomous Logistics Optimization Engine.
    """

    def __init__(self) -> None:
        """
        Initialize the constants.
        """
        self.non_stationary_drift_index: float = 0.5
        self.stochastic_regime_switch: bool = True
        self.agentic_workflow_threshold: float = 0.8
        self.langfuse_state_graph: StateGraph = StateGraph()
        self.deepeval_evaluation_metrics: EvaluationMetrics = EvaluationMetrics()

    def get_non_stationary_drift_index(self) -> float:
        """
        Get the non-stationary drift index.

        Returns:
            float: The non-stationary drift index.
        """
        try:
            logger.info('Getting non-stationary drift index')
            return self.non_stationary_drift_index
        except Exception as e:
            logger.error(f'Error getting non-stationary drift index: {e}')
            raise

    def get_stochastic_regime_switch(self) -> bool:
        """
        Get the stochastic regime switch.

        Returns:
            bool: The stochastic regime switch.
        """
        try:
            logger.info('Getting stochastic regime switch')
            return self.stochastic_regime_switch
        except Exception as e:
            logger.error(f'Error getting stochastic regime switch: {e}')
            raise

    def get_agentic_workflow_threshold(self) -> float:
        """
        Get the agentic workflow threshold.

        Returns:
            float: The agentic workflow threshold.
        """
        try:
            logger.info('Getting agentic workflow threshold')
            return self.agentic_workflow_threshold
        except Exception as e:
            logger.error(f'Error getting agentic workflow threshold: {e}')
            raise

    def get_langfuse_state_graph(self) -> StateGraph:
        """
        Get the Langfuse state graph.

        Returns:
            StateGraph: The Langfuse state graph.
        """
        try:
            logger.info('Getting Langfuse state graph')
            return self.langfuse_state_graph
        except Exception as e:
            logger.error(f'Error getting Langfuse state graph: {e}')
            raise

    def get_deepeval_evaluation_metrics(self) -> EvaluationMetrics:
        """
        Get the DeepEval evaluation metrics.

        Returns:
            EvaluationMetrics: The DeepEval evaluation metrics.
        """
        try:
            logger.info('Getting DeepEval evaluation metrics')
            return self.deepeval_evaluation_metrics
        except Exception as e:
            logger.error(f'Error getting DeepEval evaluation metrics: {e}')
            raise

def simulate_rocket_science_problem(constants: Constants) -> None:
    """
    Simulate the 'Rocket Science' problem.

    Args:
        constants (Constants): The constants to use for the simulation.
    """
    try:
        logger.info('Simulating Rocket Science problem')
        non_stationary_drift_index = constants.get_non_stationary_drift_index()
        stochastic_regime_switch = constants.get_stochastic_regime_switch()
        agentic_workflow_threshold = constants.get_agentic_workflow_threshold()
        langfuse_state_graph = constants.get_langfuse_state_graph()
        deepeval_evaluation_metrics = constants.get_deepeval_evaluation_metrics()

        # Simulate the Rocket Science problem using the constants
        logger.info(f'Non-stationary drift index: {non_stationary_drift_index}')
        logger.info(f'Stochastic regime switch: {stochastic_regime_switch}')
        logger.info(f'Agentic workflow threshold: {agentic_workflow_threshold}')
        logger.info(f'Langfuse state graph: {langfuse_state_graph}')
        logger.info(f'DeepEval evaluation metrics: {deepeval_evaluation_metrics}')
    except Exception as e:
        logger.error(f'Error simulating Rocket Science problem: {e}')
        raise

if __name__ == '__main__':
    constants = Constants()
    simulate_rocket_science_problem(constants)
",
        "commit_message": "feat: implement specialized constants logic"
    }
}
```