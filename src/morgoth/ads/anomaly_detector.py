

class AnomalyDetector(object):
    """
    This class is responsible for dectecting anomalies in metrics

    A single instance of this class will watch many metrics
    """
    def __init__(self):
        self._metrics = []

    def watch_metric(self, metric):
        """ Called when a this AD should watch a new metric """
        self._metrics.append(metric)

    def new_value(self, metric, value):
        """
        Called when a given metric receives data

        NOTE: This method is not yet called. It will be supported
        eventually
        """
        pass


    def is_anomalous(self, metric, start, end):
        """
        Return whether the given time range is anomalous

        @param metric: the name of the metric to analyze
        @param start: datetime - marks the start time to analyze
        @param end: datetime - marks the end time to analyze
        @return window - a window object indicating whether it is anomalous
        """
        raise NotImplementedError("%s.is_anomalous is not implemented" % self.__class__.__name__)

