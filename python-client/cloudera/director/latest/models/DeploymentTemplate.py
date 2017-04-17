#!/usr/bin/env python

# Licensed to Cloudera, Inc. under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  Cloudera, Inc. licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Note: This file is auto generated. Do not edit manually.

class DeploymentTemplate:

    def __init__(self, **kwargs):
        self.swaggerTypes = {
            'billingId': 'str',
            'configs': 'dict[str,dict[str,str]]',
            'csds': 'list[str]',
            'enableEnterpriseTrial': 'bool',
            'externalDatabaseTemplates': 'dict[str,cloudera.director.latest.models.ExternalDatabaseTemplate]',
            'externalDatabases': 'dict[str,cloudera.director.latest.models.ExternalDatabase]',
            'hostname': 'str',
            'javaInstallationStrategy': 'str',
            'krbAdminPassword': 'str',
            'krbAdminUsername': 'str',
            'license': 'str',
            'managerVirtualInstance': 'cloudera.director.latest.models.VirtualInstance',
            'name': 'str',
            'password': 'str',
            'port': 'int',
            'postCreateScripts': 'list[str]',
            'repository': 'str',
            'repositoryKeyUrl': 'str',
            'unlimitedJce': 'bool',
            'username': 'str'

        }


        #BillingId for Cloudera Manager [redacted on read]
        self.billingId = kwargs.get('billingId',None) # str
        #Optional configurations for Cloudera Manager and its management services
        self.configs = kwargs.get('configs',{}) # dict[str,dict[str,str]]
        #A list of CSD package URLs
        self.csds = kwargs.get('csds',[]) # list[str]
        #Whether to enable Cloudera Enterprise Trial
        self.enableEnterpriseTrial = kwargs.get('enableEnterpriseTrial',None) # bool
        #External database template definitions
        self.externalDatabaseTemplates = kwargs.get('externalDatabaseTemplates',{}) # dict[str,cloudera.director.latest.models.ExternalDatabaseTemplate]
        #External database definitions
        self.externalDatabases = kwargs.get('externalDatabases',{}) # dict[str,cloudera.director.latest.models.ExternalDatabase]
        #Hostname for existing Cloudera Manager installation
        self.hostname = kwargs.get('hostname',None) # str
        #Cloudera Director and Cloudera Manager's Java installation strategy
        self.javaInstallationStrategy = kwargs.get('javaInstallationStrategy',None) # str
        #Password for Kerberos administrative principal used by Cloudera Manager [redacted on read]
        self.krbAdminPassword = kwargs.get('krbAdminPassword',None) # str
        #Username for Kerberos administrative principal used by Cloudera Manager
        self.krbAdminUsername = kwargs.get('krbAdminUsername',None) # str
        #License for Cloudera Manager [redacted on read]
        self.license = kwargs.get('license',None) # str
        #Instance definition for a Cloudera Manager instance created from scratch
        self.managerVirtualInstance = kwargs.get('managerVirtualInstance',None) # cloudera.director.latest.models.VirtualInstance
        #Deployment name
        self.name = kwargs.get('name',None) # str
        #Web UI and API password [redacted on read]
        self.password = kwargs.get('password',None) # str
        #Port for existing Cloudera Manager installation
        self.port = kwargs.get('port',None) # int
        #A list of scripts to be run after deployment creation
        self.postCreateScripts = kwargs.get('postCreateScripts',[]) # list[str]
        #Custom Cloudera Manager repository URL
        self.repository = kwargs.get('repository',None) # str
        #Custom Cloudera Manager public GPG key
        self.repositoryKeyUrl = kwargs.get('repositoryKeyUrl',None) # str
        #Whether to install unlimited strength JCE policy files
        self.unlimitedJce = kwargs.get('unlimitedJce',None) # bool
        #Web UI and API username
        self.username = kwargs.get('username',None) # str
        
