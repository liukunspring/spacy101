import os
import spacy
from label_studio_ml.model import LabelStudioMLBase, ModelResponse
from typing import List, Dict, Optional, Union
from label_studio_sdk.label_interface.objects import PredictionValue
import os,sys
sys.path.append(
    os.path.dirname(
    os.path.dirname(os.path.realpath(__file__)))
                )
from main import build_nlp_instance
nlp = build_nlp_instance()



class SpacyMLBackend(LabelStudioMLBase):

    # define your custom labels mapping here
    _custom_labels_mapping = {}

    def setup(self):
        self.set("model_version", f'{self.__class__.__name__}-v0.0.1')

    def predict(self, tasks: List[Dict], context: Optional[Dict] = None, **kwargs) -> Union[List[Dict], ModelResponse]:
        from_name, to_name, value = self.label_interface.get_first_tag_occurence('Labels', 'Text')
        predictions = []
        for task in tasks:
            text = self.preload_task_data(task, task['data'][value])
            doc = nlp(text)
            entities = []
            for ent in doc.ents:
                entities.append({
                    'from_name': from_name,
                    'to_name': to_name,
                    'type': 'labels',
                    'value': {
                        'start': ent.start_char,
                        'end': ent.end_char,
                        'text': ent.text,
                        'labels': [self._custom_labels_mapping.get(ent.label_, ent.label_)]
                    }
                })
            predictions.append(PredictionValue(
                result=entities,
                model_version=self.get('model_version')
            ))
            
        return ModelResponse(predictions=predictions, model_version=self.get("model_version"))