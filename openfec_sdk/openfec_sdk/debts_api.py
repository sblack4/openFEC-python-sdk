# coding: utf-8

"""
    OpenFEC

    This API allows you to explore the way candidates and committees fund their campaigns.    The FEC API is a RESTful web service supporting full-text and field-specific searches on FEC data. [Bulk downloads](https://www.fec.gov/data/advanced/?tab=bulk-data) are available on the current site. Information is tied to the underlying forms by file ID and image ID. Data is updated nightly.    There is a lot of data, but a good place to start is to use search to find interesting candidates and committees. Then, you can use their IDs to find report or line item details with the other endpoints. If you are interested in individual donors, check out contributor information in schedule_a.    Get an [API key here](https://api.data.gov/signup/). That will enable you to place up to 1,000 calls an hour. Each call is limited to 100 results per page. You can email questions, comments or a request to get a key for 120 calls per minute to [APIinfo@fec.gov](mailto:apiinfo@fec.gov). You can also ask questions and discuss the data in the [FEC data Google Group](https://groups.google.com/forum/#!forum/fec-data). API changes will also be added to this group in advance of the change.    The model definitions and schema are available at [/swagger](/swagger/). This is useful for making wrappers and exploring the data.    A few restrictions limit the way you can use FEC data. For example, you can’t use contributor lists for commercial purposes or to solicit donations. [Learn more here](https://www.fec.gov/updates/sale-or-use-contributor-information/).    [View our source code](https://github.com/fecgov/openFEC). We welcome issues and pull requests!  # noqa: E501

    The version of the OpenAPI document: 1.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401
import sys  # noqa: F401

# python 2 and python 3 compatibility library
import six

from openfec_sdk.api_client import ApiClient
from openfec_sdk.exceptions import (
    ApiTypeError,
    ApiValueError
)
from openfec_sdk.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    int,
    none_type,
    str,
    validate_and_convert_types
)
from openfec_sdk.models import inline_response_default4


class DebtsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __schedules_schedule_d_get(
            self,
            api_key='DEMO_KEY',
            **kwargs
        ):
            """schedules_schedule_d_get  # noqa: E501

             Schedule D, it shows debts and obligations owed to or by the committee that are required to be disclosed.     # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True
            >>> thread = api.schedules_schedule_d_get(api_key='DEMO_KEY', async_req=True)
            >>> result = thread.get()

            Args:
                api_key (str):  API key for https://api.data.gov. Get one at https://api.data.gov/signup. . defaults to 'DEMO_KEY', must be one of ['DEMO_KEY']

            Keyword Args:
                min_image_number (str): [optional]
                sort (str): Provide a field to sort by. Use &#x60;-&#x60; for descending order. . [optional] if omitted the server will use the default value of 'load_date'
                candidate_id ([str]):  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office. . [optional]
                max_amount_incurred (float): [optional]
                min_amount_incurred (float): [optional]
                max_payment_period (float): [optional]
                sort_nulls_last (bool): Toggle that sorts null values last. [optional] if omitted the server will use the default value of False
                min_amount (str): Filter for all amounts greater than a value.. [optional]
                max_amount (str): Filter for all amounts less than a value.. [optional]
                sort_null_only (bool): Toggle that filters out all rows having sort column that is non-null. [optional] if omitted the server will use the default value of False
                max_date (date): Maximum date. [optional]
                min_date (date): Minimum date. [optional]
                sort_hide_null (bool): Hide null values on sorted column(s).. [optional] if omitted the server will use the default value of False
                min_payment_period (float): [optional]
                per_page (int): The number of results returned per page. Defaults to 20.. [optional] if omitted the server will use the default value of 20
                image_number ([str]): The image number of the page where the schedule item is reported. [optional]
                committee_id ([str]):  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id&#39;s begin with the letter C which is followed by eight digits. . [optional]
                page (int): For paginating through results, starting at page 1. [optional] if omitted the server will use the default value of 1
                max_image_number (str): [optional]
                line_number (str): Filter for form and line number using the following format: &#x60;FORM-LINENUMBER&#x60;.  For example an argument such as &#x60;F3X-16&#x60; would filter down to all entries from form &#x60;F3X&#x60; line number &#x60;16&#x60;.. [optional]
                nature_of_debt (str): [optional]
                creditor_debtor_name ([str]): [optional]
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int): specifies the index of the server
                    that we want to use.
                    Default is 0.
                async_req (bool): execute request asynchronously

            Returns:
                inline_response_default4.InlineResponseDefault4
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index', 0)
            kwargs['api_key'] = \
                api_key
            return self.call_with_http_info(**kwargs)

        self.schedules_schedule_d_get = Endpoint(
            settings={
                'response_type': (inline_response_default4.InlineResponseDefault4,),
                'auth': [
                    'ApiKeyHeaderAuth',
                    'ApiKeyQueryAuth',
                    'apiKey'
                ],
                'endpoint_path': '/schedules/schedule_d/',
                'operation_id': 'schedules_schedule_d_get',
                'http_method': 'GET',
                'servers': [],
            },
            params_map={
                'all': [
                    'api_key',
                    'min_image_number',
                    'sort',
                    'candidate_id',
                    'max_amount_incurred',
                    'min_amount_incurred',
                    'max_payment_period',
                    'sort_nulls_last',
                    'min_amount',
                    'max_amount',
                    'sort_null_only',
                    'max_date',
                    'min_date',
                    'sort_hide_null',
                    'min_payment_period',
                    'per_page',
                    'image_number',
                    'committee_id',
                    'page',
                    'max_image_number',
                    'line_number',
                    'nature_of_debt',
                    'creditor_debtor_name',
                ],
                'required': [
                    'api_key',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'api_key':
                        (str,),
                    'min_image_number':
                        (str,),
                    'sort':
                        (str,),
                    'candidate_id':
                        ([str],),
                    'max_amount_incurred':
                        (float,),
                    'min_amount_incurred':
                        (float,),
                    'max_payment_period':
                        (float,),
                    'sort_nulls_last':
                        (bool,),
                    'min_amount':
                        (str,),
                    'max_amount':
                        (str,),
                    'sort_null_only':
                        (bool,),
                    'max_date':
                        (date,),
                    'min_date':
                        (date,),
                    'sort_hide_null':
                        (bool,),
                    'min_payment_period':
                        (float,),
                    'per_page':
                        (int,),
                    'image_number':
                        ([str],),
                    'committee_id':
                        ([str],),
                    'page':
                        (int,),
                    'max_image_number':
                        (str,),
                    'line_number':
                        (str,),
                    'nature_of_debt':
                        (str,),
                    'creditor_debtor_name':
                        ([str],),
                },
                'attribute_map': {
                    'api_key': 'api_key',
                    'min_image_number': 'min_image_number',
                    'sort': 'sort',
                    'candidate_id': 'candidate_id',
                    'max_amount_incurred': 'max_amount_incurred',
                    'min_amount_incurred': 'min_amount_incurred',
                    'max_payment_period': 'max_payment_period',
                    'sort_nulls_last': 'sort_nulls_last',
                    'min_amount': 'min_amount',
                    'max_amount': 'max_amount',
                    'sort_null_only': 'sort_null_only',
                    'max_date': 'max_date',
                    'min_date': 'min_date',
                    'sort_hide_null': 'sort_hide_null',
                    'min_payment_period': 'min_payment_period',
                    'per_page': 'per_page',
                    'image_number': 'image_number',
                    'committee_id': 'committee_id',
                    'page': 'page',
                    'max_image_number': 'max_image_number',
                    'line_number': 'line_number',
                    'nature_of_debt': 'nature_of_debt',
                    'creditor_debtor_name': 'creditor_debtor_name',
                },
                'location_map': {
                    'api_key': 'query',
                    'min_image_number': 'query',
                    'sort': 'query',
                    'candidate_id': 'query',
                    'max_amount_incurred': 'query',
                    'min_amount_incurred': 'query',
                    'max_payment_period': 'query',
                    'sort_nulls_last': 'query',
                    'min_amount': 'query',
                    'max_amount': 'query',
                    'sort_null_only': 'query',
                    'max_date': 'query',
                    'min_date': 'query',
                    'sort_hide_null': 'query',
                    'min_payment_period': 'query',
                    'per_page': 'query',
                    'image_number': 'query',
                    'committee_id': 'query',
                    'page': 'query',
                    'max_image_number': 'query',
                    'line_number': 'query',
                    'nature_of_debt': 'query',
                    'creditor_debtor_name': 'query',
                },
                'collection_format_map': {
                    'candidate_id': 'multi',
                    'image_number': 'multi',
                    'committee_id': 'multi',
                    'creditor_debtor_name': 'multi',
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__schedules_schedule_d_get
        )

        def __schedules_schedule_d_sub_id_get(
            self,
            sub_id,
            api_key='DEMO_KEY',
            **kwargs
        ):
            """schedules_schedule_d_sub_id_get  # noqa: E501

             Schedule D, it shows debts and obligations owed to or by the committee that are required to be disclosed.     # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True
            >>> thread = api.schedules_schedule_d_sub_id_get(sub_id, api_key='DEMO_KEY', async_req=True)
            >>> result = thread.get()

            Args:
                sub_id (str):
                api_key (str):  API key for https://api.data.gov. Get one at https://api.data.gov/signup. . defaults to 'DEMO_KEY', must be one of ['DEMO_KEY']

            Keyword Args:
                sort_nulls_last (bool): Toggle that sorts null values last. [optional] if omitted the server will use the default value of False
                page (int): For paginating through results, starting at page 1. [optional] if omitted the server will use the default value of 1
                sort (str): Provide a field to sort by. Use &#x60;-&#x60; for descending order. . [optional] if omitted the server will use the default value of 'load_date'
                sort_null_only (bool): Toggle that filters out all rows having sort column that is non-null. [optional] if omitted the server will use the default value of False
                sort_hide_null (bool): Hide null values on sorted column(s).. [optional] if omitted the server will use the default value of False
                per_page (int): The number of results returned per page. Defaults to 20.. [optional] if omitted the server will use the default value of 20
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int): specifies the index of the server
                    that we want to use.
                    Default is 0.
                async_req (bool): execute request asynchronously

            Returns:
                inline_response_default4.InlineResponseDefault4
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index', 0)
            kwargs['api_key'] = \
                api_key
            kwargs['sub_id'] = \
                sub_id
            return self.call_with_http_info(**kwargs)

        self.schedules_schedule_d_sub_id_get = Endpoint(
            settings={
                'response_type': (inline_response_default4.InlineResponseDefault4,),
                'auth': [
                    'ApiKeyHeaderAuth',
                    'ApiKeyQueryAuth',
                    'apiKey'
                ],
                'endpoint_path': '/schedules/schedule_d/{sub_id}/',
                'operation_id': 'schedules_schedule_d_sub_id_get',
                'http_method': 'GET',
                'servers': [],
            },
            params_map={
                'all': [
                    'api_key',
                    'sub_id',
                    'sort_nulls_last',
                    'page',
                    'sort',
                    'sort_null_only',
                    'sort_hide_null',
                    'per_page',
                ],
                'required': [
                    'api_key',
                    'sub_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'api_key':
                        (str,),
                    'sub_id':
                        (str,),
                    'sort_nulls_last':
                        (bool,),
                    'page':
                        (int,),
                    'sort':
                        (str,),
                    'sort_null_only':
                        (bool,),
                    'sort_hide_null':
                        (bool,),
                    'per_page':
                        (int,),
                },
                'attribute_map': {
                    'api_key': 'api_key',
                    'sub_id': 'sub_id',
                    'sort_nulls_last': 'sort_nulls_last',
                    'page': 'page',
                    'sort': 'sort',
                    'sort_null_only': 'sort_null_only',
                    'sort_hide_null': 'sort_hide_null',
                    'per_page': 'per_page',
                },
                'location_map': {
                    'api_key': 'query',
                    'sub_id': 'path',
                    'sort_nulls_last': 'query',
                    'page': 'query',
                    'sort': 'query',
                    'sort_null_only': 'query',
                    'sort_hide_null': 'query',
                    'per_page': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__schedules_schedule_d_sub_id_get
        )


class Endpoint(object):
    def __init__(self, settings=None, params_map=None, root_map=None,
                 headers_map=None, api_client=None, callable=None):
        """Creates an endpoint

        Args:
            settings (dict): see below key value pairs
                'response_type' (tuple/None): response type
                'auth' (list): a list of auth type keys
                'endpoint_path' (str): the endpoint path
                'operation_id' (str): endpoint string identifier
                'http_method' (str): POST/PUT/PATCH/GET etc
                'servers' (list): list of str servers that this endpoint is at
            params_map (dict): see below key value pairs
                'all' (list): list of str endpoint parameter names
                'required' (list): list of required parameter names
                'nullable' (list): list of nullable parameter names
                'enum' (list): list of parameters with enum values
                'validation' (list): list of parameters with validations
            root_map
                'validations' (dict): the dict mapping endpoint parameter tuple
                    paths to their validation dictionaries
                'allowed_values' (dict): the dict mapping endpoint parameter
                    tuple paths to their allowed_values (enum) dictionaries
                'openapi_types' (dict): param_name to openapi type
                'attribute_map' (dict): param_name to camelCase name
                'location_map' (dict): param_name to  'body', 'file', 'form',
                    'header', 'path', 'query'
                collection_format_map (dict): param_name to `csv` etc.
            headers_map (dict): see below key value pairs
                'accept' (list): list of Accept header strings
                'content_type' (list): list of Content-Type header strings
            api_client (ApiClient) api client instance
            callable (function): the function which is invoked when the
                Endpoint is called
        """
        self.settings = settings
        self.params_map = params_map
        self.params_map['all'].extend([
            'async_req',
            '_host_index',
            '_preload_content',
            '_request_timeout',
            '_return_http_data_only',
            '_check_input_type',
            '_check_return_type'
        ])
        self.params_map['nullable'].extend(['_request_timeout'])
        self.validations = root_map['validations']
        self.allowed_values = root_map['allowed_values']
        self.openapi_types = root_map['openapi_types']
        extra_types = {
            'async_req': (bool,),
            '_host_index': (int,),
            '_preload_content': (bool,),
            '_request_timeout': (none_type, int, (int,), [int]),
            '_return_http_data_only': (bool,),
            '_check_input_type': (bool,),
            '_check_return_type': (bool,)
        }
        self.openapi_types.update(extra_types)
        self.attribute_map = root_map['attribute_map']
        self.location_map = root_map['location_map']
        self.collection_format_map = root_map['collection_format_map']
        self.headers_map = headers_map
        self.api_client = api_client
        self.callable = callable

    def __validate_inputs(self, kwargs):
        for param in self.params_map['enum']:
            if param in kwargs:
                check_allowed_values(
                    self.allowed_values,
                    (param,),
                    kwargs[param]
                )

        for param in self.params_map['validation']:
            if param in kwargs:
                check_validations(
                    self.validations,
                    (param,),
                    kwargs[param]
                )

        if kwargs['_check_input_type'] is False:
            return

        for key, value in six.iteritems(kwargs):
            fixed_val = validate_and_convert_types(
                value,
                self.openapi_types[key],
                [key],
                False,
                kwargs['_check_input_type'],
                configuration=self.api_client.configuration
            )
            kwargs[key] = fixed_val

    def __gather_params(self, kwargs):
        params = {
            'body': None,
            'collection_format': {},
            'file': {},
            'form': [],
            'header': {},
            'path': {},
            'query': []
        }

        for param_name, param_value in six.iteritems(kwargs):
            param_location = self.location_map.get(param_name)
            if param_location is None:
                continue
            if param_location:
                if param_location == 'body':
                    params['body'] = param_value
                    continue
                base_name = self.attribute_map[param_name]
                if (param_location == 'form' and
                        self.openapi_types[param_name] == (file_type,)):
                    params['file'][param_name] = [param_value]
                elif (param_location == 'form' and
                        self.openapi_types[param_name] == ([file_type],)):
                    # param_value is already a list
                    params['file'][param_name] = param_value
                elif param_location in {'form', 'query'}:
                    param_value_full = (base_name, param_value)
                    params[param_location].append(param_value_full)
                if param_location not in {'form', 'query'}:
                    params[param_location][base_name] = param_value
                collection_format = self.collection_format_map.get(param_name)
                if collection_format:
                    params['collection_format'][base_name] = collection_format

        return params

    def __call__(self, *args, **kwargs):
        """ This method is invoked when endpoints are called
        Example:
        pet_api = PetApi()
        pet_api.add_pet  # this is an instance of the class Endpoint
        pet_api.add_pet()  # this invokes pet_api.add_pet.__call__()
        which then invokes the callable functions stored in that endpoint at
        pet_api.add_pet.callable or self.callable in this class
        """
        return self.callable(self, *args, **kwargs)

    def call_with_http_info(self, **kwargs):

        try:
            _host = self.settings['servers'][kwargs['_host_index']]
        except IndexError:
            if self.settings['servers']:
                raise ApiValueError(
                    'Invalid host index. Must be 0 <= index < %s' %
                    len(self.settings['servers'])
                )
            _host = None

        for key, value in six.iteritems(kwargs):
            if key not in self.params_map['all']:
                raise ApiTypeError(
                    "Got an unexpected parameter '%s'"
                    ' to method `%s`' %
                    (key, self.settings['operation_id'])
                )
            # only throw this nullable ApiValueError if _check_input_type
            # is False, if _check_input_type==True we catch this case
            # in self.__validate_inputs
            if (key not in self.params_map['nullable'] and value is None
                    and kwargs['_check_input_type'] is False):
                raise ApiValueError(
                    'Value may not be None for non-nullable parameter `%s`'
                    ' when calling `%s`' %
                    (key, self.settings['operation_id'])
                )

        for key in self.params_map['required']:
            if key not in kwargs.keys():
                raise ApiValueError(
                    'Missing the required parameter `%s` when calling '
                    '`%s`' % (key, self.settings['operation_id'])
                )

        self.__validate_inputs(kwargs)

        params = self.__gather_params(kwargs)

        accept_headers_list = self.headers_map['accept']
        if accept_headers_list:
            params['header']['Accept'] = self.api_client.select_header_accept(
                accept_headers_list)

        content_type_headers_list = self.headers_map['content_type']
        if content_type_headers_list:
            header_list = self.api_client.select_header_content_type(
                content_type_headers_list)
            params['header']['Content-Type'] = header_list

        return self.api_client.call_api(
            self.settings['endpoint_path'], self.settings['http_method'],
            params['path'],
            params['query'],
            params['header'],
            body=params['body'],
            post_params=params['form'],
            files=params['file'],
            response_type=self.settings['response_type'],
            auth_settings=self.settings['auth'],
            async_req=kwargs['async_req'],
            _check_type=kwargs['_check_return_type'],
            _return_http_data_only=kwargs['_return_http_data_only'],
            _preload_content=kwargs['_preload_content'],
            _request_timeout=kwargs['_request_timeout'],
            _host=_host,
            collection_formats=params['collection_format'])
