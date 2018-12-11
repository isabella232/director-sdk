# coding: utf-8

"""
Licensed to Cloudera, Inc. under one
or more contributor license agreements.  See the NOTICE file
distributed with this work for additional information
regarding copyright ownership.  Cloudera, Inc. licenses this file
to you under the Apache License, Version 2.0 (the
"License"); you may not use this file except in compliance
with the License.  You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""


import pprint
import re  # noqa: F401

import six


class ClusterTemplate(object):
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
        'external_database_templates': 'dict(str, ExternalDatabaseTemplate)',
        'external_databases': 'dict(str, ExternalDatabase)',
        'instance_post_create_scripts': 'list[str]',
        'migrations': 'list[Migration]',
        'name': 'str',
        'parcel_repositories': 'list[str]',
        'post_create_scripts': 'list[str]',
        'pre_terminate_scripts': 'list[str]',
        'product_versions': 'dict(str, str)',
        'redeploy_client_configs_on_update': 'bool',
        'restart_cluster_on_update': 'bool',
        'services': 'list[str]',
        'services_configs': 'dict(str, dict(str, str))',
        'virtual_instance_groups': 'dict(str, VirtualInstanceGroup)'
    }

    attribute_map = {
        'external_database_templates': 'externalDatabaseTemplates',
        'external_databases': 'externalDatabases',
        'instance_post_create_scripts': 'instancePostCreateScripts',
        'migrations': 'migrations',
        'name': 'name',
        'parcel_repositories': 'parcelRepositories',
        'post_create_scripts': 'postCreateScripts',
        'pre_terminate_scripts': 'preTerminateScripts',
        'product_versions': 'productVersions',
        'redeploy_client_configs_on_update': 'redeployClientConfigsOnUpdate',
        'restart_cluster_on_update': 'restartClusterOnUpdate',
        'services': 'services',
        'services_configs': 'servicesConfigs',
        'virtual_instance_groups': 'virtualInstanceGroups'
    }

    def __init__(self, external_database_templates=None, external_databases=None, instance_post_create_scripts=None, migrations=None, name=None, parcel_repositories=None, post_create_scripts=None, pre_terminate_scripts=None, product_versions=None, redeploy_client_configs_on_update=None, restart_cluster_on_update=None, services=None, services_configs=None, virtual_instance_groups=None):  # noqa: E501
        """ClusterTemplate - a model defined in Swagger"""  # noqa: E501

        self._external_database_templates = None
        self._external_databases = None
        self._instance_post_create_scripts = None
        self._migrations = None
        self._name = None
        self._parcel_repositories = None
        self._post_create_scripts = None
        self._pre_terminate_scripts = None
        self._product_versions = None
        self._redeploy_client_configs_on_update = None
        self._restart_cluster_on_update = None
        self._services = None
        self._services_configs = None
        self._virtual_instance_groups = None
        self.discriminator = None

        if external_database_templates is not None:
            self.external_database_templates = external_database_templates
        if external_databases is not None:
            self.external_databases = external_databases
        if instance_post_create_scripts is not None:
            self.instance_post_create_scripts = instance_post_create_scripts
        if migrations is not None:
            self.migrations = migrations
        self.name = name
        if parcel_repositories is not None:
            self.parcel_repositories = parcel_repositories
        if post_create_scripts is not None:
            self.post_create_scripts = post_create_scripts
        if pre_terminate_scripts is not None:
            self.pre_terminate_scripts = pre_terminate_scripts
        if product_versions is not None:
            self.product_versions = product_versions
        if redeploy_client_configs_on_update is not None:
            self.redeploy_client_configs_on_update = redeploy_client_configs_on_update
        if restart_cluster_on_update is not None:
            self.restart_cluster_on_update = restart_cluster_on_update
        if services is not None:
            self.services = services
        if services_configs is not None:
            self.services_configs = services_configs
        self.virtual_instance_groups = virtual_instance_groups

    @property
    def external_database_templates(self):
        """Gets the external_database_templates of this ClusterTemplate.  # noqa: E501

        Optional external database templates  # noqa: E501

        :return: The external_database_templates of this ClusterTemplate.  # noqa: E501
        :rtype: dict(str, ExternalDatabaseTemplate)
        """
        return self._external_database_templates

    @external_database_templates.setter
    def external_database_templates(self, external_database_templates):
        """Sets the external_database_templates of this ClusterTemplate.

        Optional external database templates  # noqa: E501

        :param external_database_templates: The external_database_templates of this ClusterTemplate.  # noqa: E501
        :type: dict(str, ExternalDatabaseTemplate)
        """

        self._external_database_templates = external_database_templates

    @property
    def external_databases(self):
        """Gets the external_databases of this ClusterTemplate.  # noqa: E501

        Optional external databases  # noqa: E501

        :return: The external_databases of this ClusterTemplate.  # noqa: E501
        :rtype: dict(str, ExternalDatabase)
        """
        return self._external_databases

    @external_databases.setter
    def external_databases(self, external_databases):
        """Sets the external_databases of this ClusterTemplate.

        Optional external databases  # noqa: E501

        :param external_databases: The external_databases of this ClusterTemplate.  # noqa: E501
        :type: dict(str, ExternalDatabase)
        """

        self._external_databases = external_databases

    @property
    def instance_post_create_scripts(self):
        """Gets the instance_post_create_scripts of this ClusterTemplate.  # noqa: E501

        A list of scripts to be run after cluster creation on all cluster instances  # noqa: E501

        :return: The instance_post_create_scripts of this ClusterTemplate.  # noqa: E501
        :rtype: list[str]
        """
        return self._instance_post_create_scripts

    @instance_post_create_scripts.setter
    def instance_post_create_scripts(self, instance_post_create_scripts):
        """Sets the instance_post_create_scripts of this ClusterTemplate.

        A list of scripts to be run after cluster creation on all cluster instances  # noqa: E501

        :param instance_post_create_scripts: The instance_post_create_scripts of this ClusterTemplate.  # noqa: E501
        :type: list[str]
        """

        self._instance_post_create_scripts = instance_post_create_scripts

    @property
    def migrations(self):
        """Gets the migrations of this ClusterTemplate.  # noqa: E501

        A description of current manual migrations (read only)  # noqa: E501

        :return: The migrations of this ClusterTemplate.  # noqa: E501
        :rtype: list[Migration]
        """
        return self._migrations

    @migrations.setter
    def migrations(self, migrations):
        """Sets the migrations of this ClusterTemplate.

        A description of current manual migrations (read only)  # noqa: E501

        :param migrations: The migrations of this ClusterTemplate.  # noqa: E501
        :type: list[Migration]
        """

        self._migrations = migrations

    @property
    def name(self):
        """Gets the name of this ClusterTemplate.  # noqa: E501

        Cluster name  # noqa: E501

        :return: The name of this ClusterTemplate.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ClusterTemplate.

        Cluster name  # noqa: E501

        :param name: The name of this ClusterTemplate.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def parcel_repositories(self):
        """Gets the parcel_repositories of this ClusterTemplate.  # noqa: E501

        Optional set of cluster parcel repositories  # noqa: E501

        :return: The parcel_repositories of this ClusterTemplate.  # noqa: E501
        :rtype: list[str]
        """
        return self._parcel_repositories

    @parcel_repositories.setter
    def parcel_repositories(self, parcel_repositories):
        """Sets the parcel_repositories of this ClusterTemplate.

        Optional set of cluster parcel repositories  # noqa: E501

        :param parcel_repositories: The parcel_repositories of this ClusterTemplate.  # noqa: E501
        :type: list[str]
        """

        self._parcel_repositories = parcel_repositories

    @property
    def post_create_scripts(self):
        """Gets the post_create_scripts of this ClusterTemplate.  # noqa: E501

        A list of scripts to be run after cluster creation  # noqa: E501

        :return: The post_create_scripts of this ClusterTemplate.  # noqa: E501
        :rtype: list[str]
        """
        return self._post_create_scripts

    @post_create_scripts.setter
    def post_create_scripts(self, post_create_scripts):
        """Sets the post_create_scripts of this ClusterTemplate.

        A list of scripts to be run after cluster creation  # noqa: E501

        :param post_create_scripts: The post_create_scripts of this ClusterTemplate.  # noqa: E501
        :type: list[str]
        """

        self._post_create_scripts = post_create_scripts

    @property
    def pre_terminate_scripts(self):
        """Gets the pre_terminate_scripts of this ClusterTemplate.  # noqa: E501

        A list of scripts to be run before cluster termination  # noqa: E501

        :return: The pre_terminate_scripts of this ClusterTemplate.  # noqa: E501
        :rtype: list[str]
        """
        return self._pre_terminate_scripts

    @pre_terminate_scripts.setter
    def pre_terminate_scripts(self, pre_terminate_scripts):
        """Sets the pre_terminate_scripts of this ClusterTemplate.

        A list of scripts to be run before cluster termination  # noqa: E501

        :param pre_terminate_scripts: The pre_terminate_scripts of this ClusterTemplate.  # noqa: E501
        :type: list[str]
        """

        self._pre_terminate_scripts = pre_terminate_scripts

    @property
    def product_versions(self):
        """Gets the product_versions of this ClusterTemplate.  # noqa: E501

        Versions for cluster products  # noqa: E501

        :return: The product_versions of this ClusterTemplate.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._product_versions

    @product_versions.setter
    def product_versions(self, product_versions):
        """Sets the product_versions of this ClusterTemplate.

        Versions for cluster products  # noqa: E501

        :param product_versions: The product_versions of this ClusterTemplate.  # noqa: E501
        :type: dict(str, str)
        """

        self._product_versions = product_versions

    @property
    def redeploy_client_configs_on_update(self):
        """Gets the redeploy_client_configs_on_update of this ClusterTemplate.  # noqa: E501

        Whether to redeploy client configuration on cluster update  # noqa: E501

        :return: The redeploy_client_configs_on_update of this ClusterTemplate.  # noqa: E501
        :rtype: bool
        """
        return self._redeploy_client_configs_on_update

    @redeploy_client_configs_on_update.setter
    def redeploy_client_configs_on_update(self, redeploy_client_configs_on_update):
        """Sets the redeploy_client_configs_on_update of this ClusterTemplate.

        Whether to redeploy client configuration on cluster update  # noqa: E501

        :param redeploy_client_configs_on_update: The redeploy_client_configs_on_update of this ClusterTemplate.  # noqa: E501
        :type: bool
        """

        self._redeploy_client_configs_on_update = redeploy_client_configs_on_update

    @property
    def restart_cluster_on_update(self):
        """Gets the restart_cluster_on_update of this ClusterTemplate.  # noqa: E501

        Whether to restart the cluster on cluster update  # noqa: E501

        :return: The restart_cluster_on_update of this ClusterTemplate.  # noqa: E501
        :rtype: bool
        """
        return self._restart_cluster_on_update

    @restart_cluster_on_update.setter
    def restart_cluster_on_update(self, restart_cluster_on_update):
        """Sets the restart_cluster_on_update of this ClusterTemplate.

        Whether to restart the cluster on cluster update  # noqa: E501

        :param restart_cluster_on_update: The restart_cluster_on_update of this ClusterTemplate.  # noqa: E501
        :type: bool
        """

        self._restart_cluster_on_update = restart_cluster_on_update

    @property
    def services(self):
        """Gets the services of this ClusterTemplate.  # noqa: E501

        Cluster services  # noqa: E501

        :return: The services of this ClusterTemplate.  # noqa: E501
        :rtype: list[str]
        """
        return self._services

    @services.setter
    def services(self, services):
        """Sets the services of this ClusterTemplate.

        Cluster services  # noqa: E501

        :param services: The services of this ClusterTemplate.  # noqa: E501
        :type: list[str]
        """

        self._services = services

    @property
    def services_configs(self):
        """Gets the services_configs of this ClusterTemplate.  # noqa: E501

        Cluster services configurations  # noqa: E501

        :return: The services_configs of this ClusterTemplate.  # noqa: E501
        :rtype: dict(str, dict(str, str))
        """
        return self._services_configs

    @services_configs.setter
    def services_configs(self, services_configs):
        """Sets the services_configs of this ClusterTemplate.

        Cluster services configurations  # noqa: E501

        :param services_configs: The services_configs of this ClusterTemplate.  # noqa: E501
        :type: dict(str, dict(str, str))
        """

        self._services_configs = services_configs

    @property
    def virtual_instance_groups(self):
        """Gets the virtual_instance_groups of this ClusterTemplate.  # noqa: E501

        List of virtual instances  # noqa: E501

        :return: The virtual_instance_groups of this ClusterTemplate.  # noqa: E501
        :rtype: dict(str, VirtualInstanceGroup)
        """
        return self._virtual_instance_groups

    @virtual_instance_groups.setter
    def virtual_instance_groups(self, virtual_instance_groups):
        """Sets the virtual_instance_groups of this ClusterTemplate.

        List of virtual instances  # noqa: E501

        :param virtual_instance_groups: The virtual_instance_groups of this ClusterTemplate.  # noqa: E501
        :type: dict(str, VirtualInstanceGroup)
        """
        if virtual_instance_groups is None:
            raise ValueError("Invalid value for `virtual_instance_groups`, must not be `None`")  # noqa: E501

        self._virtual_instance_groups = virtual_instance_groups

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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ClusterTemplate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other