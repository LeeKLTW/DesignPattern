# -*- coding: utf-8 -*-
import json
import xml.etree.ElementTree as etree


class JSONDataExtractor:
    def __init__(self, filepath):
        self.data = dict()
        with open(filepath, 'r', encoding='utf-8') as f:
            s = f.readlines()
            self.data = json.loads(s)

    @property
    def parsed_data(self):
        return self.data


class XMLDataExtractor:
    def __init__(self, filepath):
        self.tree = etree.parse(filepath)

    @property
    def parsed_data(self):
        return self.tree


def data_extraction_factory(filepath):
    if filepath.endswith('json'):
        extractor= JSONDataExtractor
    elif filepath.endswith('xml'):
        extractor= XMLDataExtractor
    else:
        raise ValueError(f"Can't extract from {filepath}")
    return extractor(filepath)


def extract_data_from(filepath):
    factory_obj = None
    try:
        factory_obj = data_extraction_factory(filepath)
    except ValueError as e:
        print(e)
    return factory_obj
