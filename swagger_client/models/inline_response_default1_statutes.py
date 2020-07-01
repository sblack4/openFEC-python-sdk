# coding: utf-8

"""
    OpenFEC

    This API allows you to explore the way candidates and committees fund their campaigns.    The FEC API is a RESTful web service supporting full-text and field-specific searches on FEC data. [Bulk downloads](https://www.fec.gov/data/advanced/?tab=bulk-data) are available on the current site. Information is tied to the underlying forms by file ID and image ID. Data is updated nightly.    There is a lot of data, but a good place to start is to use search to find interesting candidates and committees. Then, you can use their IDs to find report or line item details with the other endpoints. If you are interested in individual donors, check out contributor information in schedule_a.    Get an [API key here](https://api.data.gov/signup/). That will enable you to place up to 1,000 calls an hour. Each call is limited to 100 results per page. You can email questions, comments or a request to get a key for 120 calls per minute to [APIinfo@fec.gov](mailto:apiinfo@fec.gov). You can also ask questions and discuss the data in the [FEC data Google Group](https://groups.google.com/forum/#!forum/fec-data). API changes will also be added to this group in advance of the change.    The model definitions and schema are available at [/swagger](/swagger/). This is useful for making wrappers and exploring the data.    A few restrictions limit the way you can use FEC data. For example, you can’t use contributor lists for commercial purposes or to solicit donations. [Learn more here](https://www.fec.gov/updates/sale-or-use-contributor-information/).    [View our source code](https://github.com/fecgov/openFEC). We welcome issues and pull requests!  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class InlineResponseDefault1Statutes(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'chapter': 'str',
        'doc_id': 'str',
        'document_highlights': 'object',
        'highlights': 'list[str]',
        'name': 'str',
        'no': 'str',
        'title': 'str',
        'url': 'str'
    }

    attribute_map = {
        'chapter': 'chapter',
        'doc_id': 'doc_id',
        'document_highlights': 'document_highlights',
        'highlights': 'highlights',
        'name': 'name',
        'no': 'no',
        'title': 'title',
        'url': 'url'
    }

    def __init__(self, chapter=None, doc_id=None, document_highlights=None, highlights=None, name=None, no=None, title=None, url=None):  # noqa: E501
        """InlineResponseDefault1Statutes - a model defined in Swagger"""  # noqa: E501

        self._chapter = None
        self._doc_id = None
        self._document_highlights = None
        self._highlights = None
        self._name = None
        self._no = None
        self._title = None
        self._url = None
        self.discriminator = None

        if chapter is not None:
            self.chapter = chapter
        if doc_id is not None:
            self.doc_id = doc_id
        if document_highlights is not None:
            self.document_highlights = document_highlights
        if highlights is not None:
            self.highlights = highlights
        if name is not None:
            self.name = name
        if no is not None:
            self.no = no
        if title is not None:
            self.title = title
        if url is not None:
            self.url = url

    @property
    def chapter(self):
        """Gets the chapter of this InlineResponseDefault1Statutes.  # noqa: E501


        :return: The chapter of this InlineResponseDefault1Statutes.  # noqa: E501
        :rtype: str
        """
        return self._chapter

    @chapter.setter
    def chapter(self, chapter):
        """Sets the chapter of this InlineResponseDefault1Statutes.


        :param chapter: The chapter of this InlineResponseDefault1Statutes.  # noqa: E501
        :type: str
        """

        self._chapter = chapter

    @property
    def doc_id(self):
        """Gets the doc_id of this InlineResponseDefault1Statutes.  # noqa: E501


        :return: The doc_id of this InlineResponseDefault1Statutes.  # noqa: E501
        :rtype: str
        """
        return self._doc_id

    @doc_id.setter
    def doc_id(self, doc_id):
        """Sets the doc_id of this InlineResponseDefault1Statutes.


        :param doc_id: The doc_id of this InlineResponseDefault1Statutes.  # noqa: E501
        :type: str
        """

        self._doc_id = doc_id

    @property
    def document_highlights(self):
        """Gets the document_highlights of this InlineResponseDefault1Statutes.  # noqa: E501


        :return: The document_highlights of this InlineResponseDefault1Statutes.  # noqa: E501
        :rtype: object
        """
        return self._document_highlights

    @document_highlights.setter
    def document_highlights(self, document_highlights):
        """Sets the document_highlights of this InlineResponseDefault1Statutes.


        :param document_highlights: The document_highlights of this InlineResponseDefault1Statutes.  # noqa: E501
        :type: object
        """

        self._document_highlights = document_highlights

    @property
    def highlights(self):
        """Gets the highlights of this InlineResponseDefault1Statutes.  # noqa: E501


        :return: The highlights of this InlineResponseDefault1Statutes.  # noqa: E501
        :rtype: list[str]
        """
        return self._highlights

    @highlights.setter
    def highlights(self, highlights):
        """Sets the highlights of this InlineResponseDefault1Statutes.


        :param highlights: The highlights of this InlineResponseDefault1Statutes.  # noqa: E501
        :type: list[str]
        """

        self._highlights = highlights

    @property
    def name(self):
        """Gets the name of this InlineResponseDefault1Statutes.  # noqa: E501


        :return: The name of this InlineResponseDefault1Statutes.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this InlineResponseDefault1Statutes.


        :param name: The name of this InlineResponseDefault1Statutes.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def no(self):
        """Gets the no of this InlineResponseDefault1Statutes.  # noqa: E501


        :return: The no of this InlineResponseDefault1Statutes.  # noqa: E501
        :rtype: str
        """
        return self._no

    @no.setter
    def no(self, no):
        """Sets the no of this InlineResponseDefault1Statutes.


        :param no: The no of this InlineResponseDefault1Statutes.  # noqa: E501
        :type: str
        """

        self._no = no

    @property
    def title(self):
        """Gets the title of this InlineResponseDefault1Statutes.  # noqa: E501


        :return: The title of this InlineResponseDefault1Statutes.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this InlineResponseDefault1Statutes.


        :param title: The title of this InlineResponseDefault1Statutes.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def url(self):
        """Gets the url of this InlineResponseDefault1Statutes.  # noqa: E501


        :return: The url of this InlineResponseDefault1Statutes.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this InlineResponseDefault1Statutes.


        :param url: The url of this InlineResponseDefault1Statutes.  # noqa: E501
        :type: str
        """

        self._url = url

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(InlineResponseDefault1Statutes, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, InlineResponseDefault1Statutes):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
