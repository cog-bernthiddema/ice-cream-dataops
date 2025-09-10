YAML reference library | Cognite Documentation

Skip to main content

September [release notes](/cdf/whatsnew)

[![Cognite Docs home](/images/logos/cdf_logo_black.svg)![Cognite Docs home](/images/logos/cdf_logo_white.svg)**Docs**](/)

[Industrial tools](/cdf/industrial_tools/)

Asset performance

  * [InField](/infield_vnext/)
  * [InRobot](/inrobot/)



[Atlas AI](/cdf/atlas_ai/)[Data engineering](/cdf/data_engineering/)[Admin](/cdf/admin/)[Deploy](/cdf/deploy/)

![](https://cognite-federatedsearch.azurewebsites.net/appbar/search.png)

English

  * [Deutsch](/de/cdf/deploy/cdf_toolkit/references/resource_library)
  * [English](/cdf/deploy/cdf_toolkit/references/resource_library)
  * [Français](/fr/cdf/deploy/cdf_toolkit/references/resource_library)
  * [Español](/es/cdf/deploy/cdf_toolkit/references/resource_library)
  * [Italiano](/it/cdf/deploy/cdf_toolkit/references/resource_library)
  * [Latviešu](/lv/cdf/deploy/cdf_toolkit/references/resource_library)
  * [Nederlands](/nl/cdf/deploy/cdf_toolkit/references/resource_library)
  * [Norsk](/no/cdf/deploy/cdf_toolkit/references/resource_library)
  * [Português](/pt/cdf/deploy/cdf_toolkit/references/resource_library)
  * [Română](/ro/cdf/deploy/cdf_toolkit/references/resource_library)
  * [Svenska](/sv/cdf/deploy/cdf_toolkit/references/resource_library)
  * [한국어](/ko/cdf/deploy/cdf_toolkit/references/resource_library)
  * [中文](/zh/cdf/deploy/cdf_toolkit/references/resource_library)
  * [日本語](/ja/cdf/deploy/cdf_toolkit/references/resource_library)



![](https://cognite-federatedsearch.azurewebsites.net/appbar/app.png)

[![](https://cognite-federatedsearch.azurewebsites.net/appbar/ask.png) Cognite Hub ![](https://cognite-federatedsearch.azurewebsites.net/appbar/open.png)](https://hub.cognite.com/)[![](https://cognite-federatedsearch.azurewebsites.net/appbar/academy.png) Cognite Academy ![](https://cognite-federatedsearch.azurewebsites.net/appbar/open.png)](https://learn.cognite.com/)[![](https://cognite-federatedsearch.azurewebsites.net/appbar/statuspage.png) Cognite status page ![](https://cognite-federatedsearch.azurewebsites.net/appbar/open.png)](https://status.cognite.com/)[![](https://cognite-federatedsearch.azurewebsites.net/appbar/support.png) Cognite support ![](https://cognite-federatedsearch.azurewebsites.net/appbar/open.png)](https://cognite.zendesk.com/hc/en-us/requests/new)

###### Cognite website

[www.cognite.com![](https://cognite-federatedsearch.azurewebsites.net/appbar/open.png)](https://www.cognite.com/)

  * [Deploy Cognite Data Fusion](/cdf/deploy/)

    * [Planning](/cdf/deploy/cdf_plan/cdf_plan_intro)

    * [Deploying with the Cognite Toolkit](/cdf/deploy/cdf_toolkit/)

      * [Setting up](/cdf/deploy/cdf_toolkit/guides/setup)
      * [Upgrading](/cdf/deploy/cdf_toolkit/guides/upgrade)
      * [Configure, build, and deploy modules](/cdf/deploy/cdf_toolkit/guides/usage)
      * [Customizing modules](/cdf/deploy/cdf_toolkit/guides/modules/custom)
      * [Authentication and authorization for Cognite Toolkit](/cdf/deploy/cdf_toolkit/guides/auth)
      * [API reference](/cdf/deploy/cdf_toolkit/api/)

      * [CI/CD](/cdf/deploy/cdf_toolkit/guides/cicd/)

      * [Plugins](/cdf/deploy/cdf_toolkit/guides/plugins/)

      * [InField](/cdf/deploy/cdf_toolkit/guides/set_up_infield)

      * [InRobot](/cdf/deploy/cdf_toolkit/guides/inrobot_toolkit)

      * [Modules](/cdf/deploy/cdf_toolkit/references/packages/)

      * [YAML reference library](/cdf/deploy/cdf_toolkit/references/resource_library)



On this page

# YAML reference library

The YAML **resource configuration files** are core to the Cognite Toolkit. Each of the files configures one of the **resource types** that are supported by the Cognite Toolkit and the Cognite API. This article describes how to configure the different resource types.

The Cognite Toolkit bundles logically connected resource configuration files in **modules** , and each module stores the configuration files in directories corresponding to the resource types, called **resource directories**. The available resource directories are:
    
    
    ./<module_name>/  
             ├── 3dmodels/  
             ├── agents/ (alpha)  
             ├── auth/  
             ├── cdf_applications/  
             ├── classic/  
             ├── data_models/  
             ├── data_sets/  
             ├── extraction_pipelines/  
             ├── files/  
             ├── functions/  
             ├── hosted_extractors/  
             ├── locations/  
             ├── raw/  
             ├── robotics/  
             ├── streamlit/  
             ├── timeseries/  
             ├── transformations/  
             └── workflows/  
    

Note that a resource directory can host one or more configuration types. For example, the `data_models/` directory hosts the configuration files for spaces, containers, views, data models, and nodes. While the `classic/` directory hosts the configuration files for labels, assets, and sequences.

When you deploy, the Cognite Toolkit uses the Cognite API to implement the YAML configurations in the CDF project.

In general, the format of the YAML files matches the [API specification](https://developer.cognite.com/api/) for the resource types. We recommend that you use the `externalId` of the resources as (part of) the name of the YAML file. This is to enable using the same resource configuration across multiple CDF projects, for example, a development, staging and production project. Use number prefixes (_1. <filename.suffix>_) to control the order of deployment within each resource type.

## 3D Models​

**Resource directory:_3dmodels/_**

_Requires Cognite Toolkit v0.3.0 or later_

**API documentation:** [3D models](https://developer.cognite.com/api#tag/3D-Models/operation/create3DModels)

3D model configurations are stored in the module's _3dmodels/_ directory. You can have one or more 3D models in a single YAML file. The filename must end with `3DModel`, for example, `my_3d_model.3DModel.yaml`.

Example 3D model configuration:

my_3d_model.3DModel.yaml
    
    
    name: my_3d_model  
    dataSetExternalId: ds_3d_models  
    metadata:  
      origin: cognite-toolkit  
    

note

The 3D model API uses an **internal ID** for the `dataSetId`, while the YAML configuration files reference the **external ID** ; `dataSetExternalId`. The Cognite Toolkit resolves the external ID to the internal ID before sending the request to the Cognite API.

## Agents​

**Resource directory:_agents/_**

_Requires Cognite Toolkit v0.5.85 or later and alpha flag`agents` enabled_

**API documentation:** [Agents](https://api-docs.cognite.com/20230101-beta/tag/Agents/operation/main_ai_agents_post)

Agent configurations are stored in the module's _agents/_ directory. You can have one or more agents in a single YAML file. It's recommended to have one agent per file. The filename must end with `Agent`, for example, `my_agent.Agent.yaml`.

Example agent configuration:

my_agent.Agent.yaml
    
    
    externalId: my_agent  
    name: My Agent  
    description: This is my agent  
    instructions: This is instructions the agent.  
    model: azure/gpt-4o-mini  
    tools:  
      - type: askDocument  
        name: Document Search  
        description: Search for information in documents.  
    

### Available tools​

This section lists the available tools that you can use in the agent configuration. Note that this is a service in rapid development, and there may be more tools available than what is listed here. When you use a tool that the Cognite Toolkit doesn't recognize, you will get a warning when running the `cdf build` command. However, you can still deploy the tool to CDF as long as the CDF API supports the tool.

**Ask document**
    
    
    ...  
    - type: askDocument  
      name: Document Search  
      description: Search for information in documents.  
    

**Summarize document**
    
    
    - type: summarizeDocument  
      name: Document Summarization  
      description: Summarize the content of a document.  
    

**Ask knowledge graph**
    
    
    - type: queryKnowledgeGraph  
      name: Knowledge Graph Query  
      description: Query the knowledge graph for information.  
      configuration:  
        dataModels:  
          - space: cdf_cdm  
            externalId: CogniteCore  
            version: v1  
            viewExternalIds:  
            - CogniteAsset  
            - CogniteEquipment  
            - CogniteTimeSeries  
            - CogniteFile  
            - CogniteActivity  
        instanceSpaces:  
          type: manual  
          spaces:  
          - my_space  
          - my_other_space  
        # Or you can include all instance spaces with  
       # instanceSpaces:  
       #  type: all  
         
    

**Query time series data points**
    
    
    - type: queryTimeSeriesDatapoints  
      name: Time Series Query  
      description: Query time series data.  
    

## Assets​

**Resource directory:_classic/_**

_Requires Cognite Toolkit v0.3.0 or later_

**API documentation:** [Assets](https://developer.cognite.com/api#tag/Assets/operation/createAssets)

Asset configurations are stored in the module's _classic/_ directory. You can have one or more asset in a single YAML file. The filename must end with `Asset`, for example, `my_asset.Asset.yaml`.

Example Asset configuration:

my_root.Asset.yaml
    
    
    externalId: my_root_asset  
    name: SAP hierarchy  
    description: The root asset in the SAP hierarchy  
    dataSetExternalId: ds_sap_assets  
    source: SAP  
    metadata:  
      origin: cognite-toolkit  
    

note

The asset API uses an **internal ID** for the data set, while the YAML configuration files reference the **external ID** ; `dataSetExternalId`. The Cognite Toolkit resolves the external ID to the internal ID before sending the request to the Cognite API.

The Cognite Toolkit supports all fields in the Asset API. See below for a complete example:

my_asset.Asset.yaml
    
    
    externalId: my_asset  
    name: My asset  
    parentExternalId: my_root_asset  
    description: This is my asset  
    dataSetExternalId: ds_assets  
    source: SAP  
    metadata:  
      origin: cognite-toolkit  
      my_custom_field: my_custom_value  
    labels:  
      externalId: my_label  
    

::: note

The CogniteToolkit doesn't support the field `parentId` in the asset configuration. Instead, use `parentExternalId`. The `parentId` field is an **internal ID** that is not consistent across environments.

:::

### Table formats​

In addition to `yaml`, the Cognite Toolkit supports `csv` and `parquet` formats for asset configurations. As with the `yaml` format, the filename must end with `Asset`, for example, `my_asset.Asset.csv`.

my_root.Asset.csv
    
    
    externalId,name,description,dataSetExternalId,source,metadata.origin  
    my_root_asset,SAP hierarchy,The root asset in the SAP hierarchy,ds_sap_assets,SAP,cognite-toolkit  
    

Note that the column names must match the field names in the `yaml` configuration. The exception is the `metadata` field, which is a dictionary in the `yaml` configuration, but a string in the `csv` configuration. This is solved by using the notation `metadata.origin` column in the `csv` configuration.

## Groups​

**Resource directory:_auth/_**

**API documentation:** [Groups](https://developer.cognite.com/api#tag/Groups/operation/createGroups)

The group configuration files are stored in the module's _auth/_ directory. You can have one or more groups in a single YAML file. The filename must end with `Group`, for example, `my_group.Group.yaml`.

The `name` field is used as a unique identifier for the group. If you change the name of the group manually in CDF, it will be treated as a different group and will be ignored by the Cognite Toolkit.

**Example group configuration:**

my_group.Group.yaml
    
    
    name: 'my_group'  
    sourceId: '{{mygroup_source_id}}'  
    metadata:  
      origin: 'cognite-toolkit'  
    capabilities:  
      - projectsAcl:  
          actions:  
            - LIST  
            - READ  
          scope:  
            all: {}  
    

We recommend using the `metadata:origin` property to indicate that the group is created by the Cognite Toolkit

You can specify each ACL capability in CDF as in the `projectsAcl` example above. Scoping to dataset, space, RAW table, current user, or pipeline is also supported (see ACL scoping).

### Groups and group deletion​

If you delete groups with the `cdf clean` or `cdf deploy --drop` command, the Cognite Toolkit skips the groups that the running user or service account is a member of. This prevents the cleaning operation from removing access rights from the running user and potentially locking the user out from further operation.

### ACL scoping​

#### Dataset scope​

Use to restrict access to data in a specific **data set**.

<fragment>
    
    
    - threedAcl:  
        actions:  
          - READ  
        scope:  
          datasetScope: { ids: ['my_dataset'] }  
    

note

The groups API uses an **internal ID** for the data set, while the YAML configuration files reference the **external ID**. The Cognite Toolkit resolves the external ID to the internal ID before sending the request to the Cognite API.

#### Space scope​

Use to restrict access to data in a **data model space**.

<fragment>
    
    
    - dataModelInstancesAcl:  
        actions:  
          - READ  
        scope:  
          spaceIdScope: { spaceIds: ['my_space'] }  
    

#### Table scope​

Use to restrict access to a **database**.

<fragment>
    
    
    - rawAcl:  
        actions:  
          - READ  
          - WRITE  
        scope:  
          tableScope:  
            dbsToTables:  
              my_database: []  
    

Use to restrict access to a **table** in a database.

<fragment>
    
    
    - rawAcl:  
        actions:  
          - READ  
          - WRITE  
        scope:  
          tableScope:  
            dbsToTables:  
              my_database: ["my_table", "my_other_table"]  
    

caution

The CDF API also supports `my_database: {"tables": []}` and `my_database: {"tables": ["my_table"]}` to restrict access to all tables in a database or a specific table in a database. The Cognite Toolkit will warn you if you use these notations, because the `cdf dump group` and `cdf modules pull` commands work better with consistent YAML files. The toolkit recommends using only the list notation.

#### Current user-scope​

Use to restrict actions to the **groups the user is a member of**.

<fragment>
    
    
    - groupsAcl:  
        actions:  
          - LIST  
          - READ  
        scope:  
          currentuserscope: {}  
    

## Security categories​

_Requires Cognite Toolkit v0.2.0 or later_

**Resource directory:_auth/_**

**API documentation:** [Security categories](https://developer.cognite.com/api#tag/Security-categories/)

The security categories are stored in the module's _auth/_ directory. You can have one or more security categories in a single YAML file.

We recommend that you start security category names with `sc_` and use `_` to separate words. The file name is not significant, but we recommend that you name it after the security categories it creates.

project_categories.SecurityCategory.yaml
    
    
    - name: sc_my_security_category  
    - name: sc_my_other_security_category  
    

## Data models​

**Resource directory:_data_models/_**

**API documentation:** [Data modeling](https://developer.cognite.com/api#tag/Data-Modeling)

The data model configurations are stored in the module's __data_models__ directory.

A data model consists of a set of data modeling entities: one or more spaces, containers, views, and data models. Each entity has its own file with a suffix to indicate the entity type: _my.space.yaml_ , _my.container.yaml_ , _my.view.yaml_ , _my.datamodel.yaml_.

You can also use the Cognite Toolkit to create nodes to keep configuration for applications (for instance, InField) and to create node types that are part of the data model. Define nodes in files with the _.node.yaml_ suffix.

The Cognite Toolkit applies configurations in the order of dependencies between the entity types: first **spaces** , next **containers** , then **views** , and finally **data models**.

If there are dependencies between the entities of the same type, you can use prefix numbers in the filename to have the Cognite Toolkit apply the files in the correct order.

The Cognite Toolkit supports using subdirectories to organize the files, for example:
    
    
    data_models/  
        ┣ 📂 containers/  
        ┣ 📂 views/  
        ┣ 📂 nodes/  
        ┣ 📜 my_data_model.datamodel.yaml  
        ┗ 📜 data_model_space.space.yaml  
    

### Spaces​

**API documentation:** [Spaces](https://developer.cognite.com/api#tag/Spaces/operation/ApplySpaces)

Spaces are the top-level entities and is the home of containers, views, and data models. You can create a space with a _.space.yaml_ file in the _data_models/_ directory.

sp_cognite_app_data.space.yaml
    
    
    space: sp_cognite_app_data  
    name: cognite:app:data  
    description: Space for InField app data  
    

CDF doesn't allow a space to be deleted unless it's empty. If a space contains, for example, nodes that aren't governed by the Cognite Toolkit, the Cognite Toolkit will not delete the space.

### Containers​

**API documentation:** [Containers](https://developer.cognite.com/api#tag/Containers/operation/ApplyContainers)

Containers are the home of properties and data. You can create a container with a _.container.yaml_ file in the _data_models/_ directory. You can also create indexes and constraints according to the API specification.

MyActivity.container.yaml
    
    
    externalId: MyActivity  
    usedFor: node  
    space: sp_activity_data  
    description: 'A container for activity data.'  
    name: The display name of the container  
    properties:  
      id:  
        type:  
          type: text  
          list: false  
          collation: ucs_basic  
        nullable: true  
        immutable: false  
        autoIncrement: false  
      title:  
        type:  
          type: text  
          list: false  
          collation: ucs_basic  
        nullable: true  
        defaultValue: No title  
        description: The title of the activity  
        name: Display name of the title property  
      description:  
        type:  
          type: text  
          list: false  
          collation: ucs_basic  
        nullable: true  
      asset:  
        type:  
          type: direct  
          list: false  
        nullable: true  
        description: The asset the activity is related to  
    indexes:  
      idLookup:  
        properties:  
          - id  
        indexType: btree  
        cursorable: true  
    constraints:  
      idUnique:  
        constraintType: uniqueness  
        properties:  
          - id  
    

The example container definition creates a container with the properties `id`, `title`, `description`, and `asset`.

Note that `sp_activity_data` requires its own _activity_data.space.yaml_ file in the _data_models/_ directory.

### Views​

**API documentation:** [Views](https://developer.cognite.com/api#tag/Views/operation/ApplyViews)

Use views to ingest, query, and structure the data into meaningful entities in your data model. You can create a view with a _.view.yaml_ file in the _data_models/_ directory.

MyActivity.view.yaml
    
    
    externalId: MyActivity  
    name: MyActivity  
    description: 'An activity represents a set of maintenance tasks with multiple operations for individual assets. The activity is considered incomplete until all its operations are finished.'  
    version: '3'  
    space: sp_activity_model  
    implements:  
      - type: view  
        externalId: CogniteActivity  
        space: cdf_cdm  
        version: v1  
    properties:  
      id:  
        description: 'Unique identifier from the source, for instance, an object ID in SAP.'  
        container:  
          type: container  
          space: sp_activity_data  
          externalId: MyActivity  
        containerPropertyIdentifier: id  
      title:  
        description: 'A title or brief description of the maintenance activity or work order.'  
        container:  
          type: container  
          space: sp_activity_data  
          externalId: MyActivity  
        containerPropertyIdentifier: title  
      description:  
        description: 'A detailed description of the maintenance activity or work order.'  
        container:  
          type: container  
          space: sp_activity_data  
          externalId: MyActivity  
        containerPropertyIdentifier: description  
      asset:  
        description: 'The asset the activity is related to.'  
        container:  
          type: container  
          space: sp_activity_data  
          externalId: MyActivity  
        containerPropertyIdentifier: asset  
        source:  
          type: view  
          externalId: MyAsset  
          space: sp_activity_model  
          version: '2'  
    

This example view configuration creates a view with the properties `id`, `title`, `description`, and `asset`. The `asset` property references the `MyAsset` view in the `sp_activity_model` space.

The view references the properties from the container `MyActivity` in the `sp_activity_data` space. The view exists in a space called `sp_activity_model`, while the container exists in the `sp_activity_data` space.

### Data models​

**API documentation:** [Data models](https://developer.cognite.com/api#tag/Data-models/operation/createDataModels)

Use data models to structure the data into knowledge graphs with relationships between views using edges. From an implementation perspective, a data model is a collection of views.

You can create a data model with a _.datamodel.yaml_ file in the _data_models/_ directory.

ActivityDataModel.datamodel.yaml
    
    
    externalId: ActivityDataModel  
    name: My activity data model  
    version: '1'  
    space: sp_activity_model  
    description: 'A data model for structuring and querying activity data.'  
    views:  
      - type: view  
        externalId: MyActivity  
        space: sp_activity_model  
        version: '3'  
      - type: view  
        externalId: MyTask  
        space: sp_activity_model  
        version: '2'  
    

The example data model configuration creates a data model with two views: `MyActivity` and `MyTasks`. The data model exists in a space called `sp_activity_model` together with the views.

### Nodes​

**API documentation:** [Instances](https://developer.cognite.com/api#tag/Instances/operation/applyNodeAndEdges)

Use nodes to populate a data model. You can create nodes with a _.node.yaml_ file in the _data_models/_ directory.

myapp_config.node.yaml
    
    
    - space: sp_config  
      externalId: myapp_config  
      type:  
        space: sp_config_schema  
        externalId: ConfigNode  
      sources:  
        - source:  
            space: sp_config  
            externalId: MY_APP_Config  
            version: '1'  
            type: view  
          properties:  
            rootLocationConfigurations:  
              - assetExternalId: 'my_root_asset_external_id'  
                adminGroup:  
                  - gp_template_admins  
            dataSpaceId: sp_activity_data  
            modelSpaceId: sp_activity_model  
            activityDataModelId: MyActivity  
            activityDataModelVersion: '1'  
    

This example node configuration creates a node instance with data that configures a node of the type `MY_APP_Config` with version '1' in the `sp_config` space. The instance has data that is read by MY_APP and used to configure the application.

The node instance is created in the `sp_config` space with `myapp_config` as the `externalId`. The example also configures a root location for the application and specifies how to find the application's data: in the `sp_activity_data` space with version `1` of the `MyActivity`view.

Another example is **node types**. They are part of a data model schema (the description of how data is structured), and creates a type of node that can be created in the data model. This is an example of a YAML file with multiple node types defined.

myapp_config.node.yaml
    
    
    - space: sp_my_model  
      externalId: pump  
    - space: sp_my_model  
      externalId: valve  
    - space: sp_config_schema  
      externalId: ConfigNode  
    

### Edges​

_Requires Cognite Toolkit v0.4.0 or later_

**API documentation:** [Instances](https://developer.cognite.com/api#tag/Instances/operation/applyNodeAndEdges)

Use edges to define connections between nodes in a data model. You can create edges with a _.edge.yaml_ file in the _data_models/_ directory.

You can have one or more edges in a single YAML file. The filename must end with `Edge`, for example, `my_edge.Edge.yaml`.

my_edge.Edge.yaml
    
    
    space: sp_instance  
    externalId: 'MyEdge'  
    startNode:  
      space: sp_instance  
      externalId: 'startNode'  
    endNode:  
      space: sp_instance  
      externalId: 'endNode'  
    type:  
      space: sp_schema  
      externalId: 'AnEdgeType'  
    sources:  
      - source:  
          space: sp_schema  
          externalId: 'MyView'  
          version: v1  
          type: 'view'  
        properties:  
          myProperty: 'myValue'  
    

## Data sets​

**Resource directory:_data_sets/_**

**API documentation:** [Data sets](https://developer.cognite.com/api#tag/Data-sets/operation/createDataSets)

You can not delete data sets in CDF, but you can use the Cognite Toolkit to create new data sets or update existing ones. You can create multiple data sets in the same YAML file. The filename must end with `DataSet`, for example, `my_data_set.DataSet.yaml`.

note

The data sets API uses an **internal ID** for the data set, while the YAML configuration files reference the **external ID** ; `dataSetExternalId`. The Cognite Toolkit resolves the external ID to the internal ID before sending the request to the Cognite API. For an example, see files.

data_sets.DataSet.yaml
    
    
    - externalId: ds_asset_hamburg  
      name: asset:hamburg  
      description: This dataset contains asset data for the Hamburg location.  
      writeProtected: false  
      metadata:  
        origin: cognite-toolkit  
    - externalId: ds_files_hamburg  
      name: files:hamburg  
      description: This dataset contains files for the Hamburg location.  
      writeProtected: false  
      metadata:  
          origin: cognite-toolkit  
    

This example configuration creates two data sets using the [naming conventions](/cdf/deploy/cdf_toolkit/references/naming_conventions) for data sets.

## Events​

_Requires Cognite Toolkit v0.4.0 or later_

**Resource directory:_classic/_**

**API documentation:** [Events](https://developer.cognite.com/api#tag/Events/operation/createEvents)

Events can be found in the module's `classic/` directory. You can define one or more events in a single YAML file. The filename must end with `Event`, for example, `my_event.Event.yaml`.

The Cognite Toolkit ensures that dependent resources are created before the events. For example, if you reference an asset or a data set in an event, the Cognite Toolkit creates the asset or data set before creating the event.

Example event definition:

my_event.Event.yaml
    
    
    externalId: MyEvent  
    dataSetExternalId: ds_complete_org  
    startTime: 1732959346052  
    endTime: 1732959346052  
    type: 'success'  
    subtype: 'info'  
    description: 'My event description'  
    metadata:  
      key: value  
    assetExternalIds:  
      - MyAsset  
      - MyAsset2  
    source: 'my_source'  
    

note

The data set is referenced by the `dataSetExternalId` and `assetExternalIds`. The Cognite Toolkit automatically resolves the external ID to the internal ID of the data set and assets before sending the request to CDF.

## InfieldV1​

_Requires Cognite Toolkit v0.5.10 or later and alpha flag`infield` enabled_

**Resource directory:_cdf_applications/_**

InfieldV1 can be found in the modules `cdf_applications/` directory. You can define one or more InfieldV1 configurations in a single YAML file. The filename must end with `InfieldV1`, for example, `my_infield_app.InfieldV1.yaml`.

The Cognite Toolkit ensures that dependent resources are created before the InfieldV1 applications. For example, if you reference a space, data sets, assets, or groups in the InfieldV1 configuration, the Cognite Toolkit creates it before creating the InfieldV1 configuration.

Example InfieldV1 configuration:

my_infield_app.InfieldV1.yaml
    
    
    externalId: default_infield_config_minimal  
    featureConfiguration:  
      rootLocationConfigurations:  
      - assetExternalId: WMT:VAL  
        appDataInstanceSpace: sp_infield_oid_app_data  
        sourceDataInstanceSpace: sp_asset_oid_source  
        templateAdmins:  
        - gp_infield_oid_template_admins  
        checklistAdmins:  
        - gp_infield_oid_checklist_admins  
        dataSetExternalId: ds_complete_org  
    customerDataSpaceId: APM_SourceData  
    customerDataSpaceVersion: '1'  
    name: Infield APM App Config  
    

note

The data set is referenced by the `dataSetExternalId`. The Cognite Toolkit automatically resolves the external ID to the internal ID of the data set.

## Labels​

_Requires Cognite Toolkit v0.3.0 or later_

**Resource directory:_classic/_** (_labels/_ in `v0.2.0`)

**API documentation:** [Labels](https://developer.cognite.com/api#tag/Labels/operation/createLabelDefinitions)

Labels can be found in the module's `classic/` directory. You can define one or more labels in a single YAML file. The filename must end with `Label`, for example, `my_equipment.Label.yaml`.

The Cognite Toolkit creates labels before files and other resources that reference them.

Example label definition:

my_equipment.Label.yaml
    
    
    - externalId: label_pump  
      name: Pump  
      description: A pump is an equipment that moves fluids.  
      dataSetExternalId: ds_labels_{{example_variable}}  
    

note

The Cognite API doesn't support updating labels. When you update a label with the Cognite Toolkit, it deletes the previous label and creates a new one.

## Extraction pipelines​

**Resource directory:_extraction_pipelines/_**

**API documentation:** [Extraction pipelines](https://developer.cognite.com/api#tag/Extraction-Pipelines/operation/createExtPipes)

**API documentation Configuration:** [Extraction pipeline config](https://developer.cognite.com/api#tag/Extraction-Pipelines-Config/operation/createExtPipeConfig)

**Documentation:** [Extraction pipeline documentation](/cdf/integration/guides/interfaces/add_integrations)

Extractor pipelines and configurations are stored in the module's _extraction_pipelines/_ directory. You can define one or more extraction pipelines in a single YAML file. It is, however, most common to have one pipeline per file. In addition, one or more the extraction pipeline configurations must be stored in a separate file. Extraction pipeline configurations are detected by the `.config` suffix, while extraction pipeline filenames end with `ExtractionPipeline`.

ep_src_asset_hamburg_sap.ExtractionPipeline.yaml
    
    
    externalId: 'ep_src_asset_hamburg_sap'  
    name: 'src:asset:hamburg:sap'  
    dataSetExternalId: 'ds_asset_{{location_name}}'  
    description: 'Asset source extraction pipeline with configuration for a DB extractor reading data from Hamburg SAP'  
    rawTables:  
      - dbName: 'asset_hamburg_sap'  
        tableName: 'assets'  
    source: 'sap'  
    documentation: "The DB Extractor is a general database extractor that connects to a database, runs one or several queries, and sends the result to CDF RAW.\n\nThe extractor connects to a database over ODBC, which means that you need an ODBC driver for your database. If you are running the Docker version of the extractor, ODBC drivers for MySQL, MS SQL, PostgreSql and Oracle DB are preinstalled in the image. See the example config for details on connection strings for these. If you are running the Windows exe version of the extractor, you must provide an ODBC driver yourself. These are typically provided by the database vendor.\n\nFurther documentation is available [here](./docs/documentation.md)\n\nFor information on development, consider the following guides:\n\n * [Development guide](guides/development.md)\n * [Release guide](guides/release.md)"  
    schedule: Continuous  
    contacts:  
      - name: 'John Doe'  
        email: john.doe@company.com  
        role: 'Extractor developer'  
        sendNotification: true  
    metadata:  
        origin: 'cognite-toolkit'  
        my_custom_field: 'my_custom_value'  
    notificationConfig:  
      allowedNotSeenRangeInMinutes: 120  
    createdBy: 'John Doe'  
    

This example configuration creates an extraction pipeline with the external ID `ep_src_asset_hamburg_sap` and the name `src:asset:hamburg:sap`.

The configuration allows an extractor installed inside a closed network to connect to CDF and download the extractor's configuration file. The Cognite Toolkit expects the configuration file be in the same directory and have the same name as the extraction pipeline configuration file, but with the suffix `.config.yaml`. The configuration file is not strictly required, but the Cognite Toolkit warns if the file is missing during the deployment process.

The extraction pipeline can be connected to a data set and to the RAW tables that the extractor will write to.

This is an example configuration file for the extraction pipeline above:

ep_src_asset_hamburg_sap.config.yaml
    
    
    externalId: 'ep_src_asset_hamburg_sap'  
    description: 'DB extractor config reading data from Hamburg SAP'  
    config:  
      logger:  
        console:  
          level: INFO  
        file:  
          level: INFO  
          path: 'file.log'  
      # List of databases  
      databases:  
        - type: odbc  
          name: postgres  
          connection-string: 'DSN={MyPostgresDsn}'  
      # List of queries  
      queries:  
        - name: test-postgres  
          database: postgres  
          query: >  
            SELECT  
    

note

The Cognite Toolkit expects the `config` property to be valid YAML and will not validate the content of the config property beyond the syntax validation. The extractor that is configured to download the configuration file validates the content of the `config` property.

## Files​

**Resource directory _files/_**

**API documentation:** [Files](https://developer.cognite.com/api#tag/Files/operation/initFileUpload)

`CogniteFile` Requires Cognite Toolkit v0.3.0 or later

caution

Use the Cognite Toolkit only to upload **example data** , and not as a general solution to ingest files into CDF.

Files can be found in the module's `files/` directory. You can define the metadata for one or more files using either a single YAML file or multiple YAML files. Mark the files as `CogniteFile` or `FileMetadata` by using the suffix `.CogniteFile.yaml` or `.FileMetadata.yaml`. Files with a suffix other than `.yaml`, such as `.txt`, or YAML files that do not end with `FileMetadata` or `CogniteFile`, are expected to be content of a configuration file.

To upload a file with the metadata, the `name` in the `YAML` file must match the filename of the file that should be uploaded.

Note: You can also use the template for uploading multiple files to upload multiple files without specifying the metadata for each file.

Below is an example of a classic file metadata configuration for multiple files, `my_file.pdf` and `my_other_file.pdf`:

my_files.FileMetadata.yaml
    
    
    - externalId: 'sharepointABC_my_file.pdf'  
      name: 'my_file.pdf'  
      source: 'sharepointABC'  
      dataSetExternalId: 'ds_files_hamburg'  
      directory: 'files'  
      mimeType: 'application/pdf'  
      metadata:  
        origin: 'cognite-toolkit'  
      assetExternalIds:  
        - 'my_root_asset'  
      sourceCreatedTime: 1640995200000  
      sourceModifiedTime: 1640995200000  
      securityCategories:  
        - 'sc_my_security_category'  
      labels:  
        - externalId: 'my_label'  
    - externalId: 'sharepointABC_my_other_file.pdf'  
      name: 'my_other_file.pdf'  
      source: 'sharepointABC'  
      dataSetExternalId: 'ds_files_hamburg'  
      directory: 'files'  
      mimeType: 'application/pdf'  
      metadata:  
        origin: 'cognite-toolkit'  
    

Classic metadata configuration for a single file, `my_file.pdf`:

my_file.FileMetadata.yaml
    
    
    externalId: 'sharepointABC_my_file.pdf'  
    name: 'my_file.pdf'  
    source: 'sharepointABC'  
    dataSetExternalId: 'ds_files_hamburg'  
    directory: 'files'  
    mimeType: 'application/pdf'  
    metadata:  
      origin: 'cdf-project-templates'  
    

note

The data set is referenced by the `dataSetExternalId`. The Cognite Toolkit automatically resolves the external ID to the internal ID of the data set.

Below is an example of a `CogniteFile` metadata configuration for a single file, `my_file.pdf`:

my_file.CogniteFile.yaml
    
    
    externalId: 'sharepointABC_my_file.pdf'  
    space: 'sp_files_hamburg'  
    name: 'my_file.pdf'  
    description: 'This is a file uploaded from SharePoint.'  
    tags:  
      - 'file'  
      - 'sharepoint'  
    sourceId: 'sharepointABC'  
    sourceContext: 'sharepointABC'  
    source:  
      space: 'sp_files_hamburg'  
      externalId: 'sharepointABCSource'  
    sourceCreatedTime: '2022-01-01T00:00:00Z'  
    sourceUpdatedTime: '2022-01-01T00:00:00Z'  
    assets:  
      - space: 'sp_assets'  
        externalId: 'my_root_asset'  
    mimeType: 'application/pdf'  
    directory: 'files'  
    category:  
      - space: 'sp_categories'  
        externalId: 'sc_my_category'  
    

Below is an example of a `CogniteFile` metadata configuration for multiple files, `my_file.pdf` and `my_other_file.pdf`:

my_files.CogniteFile.yaml
    
    
    - space: 'sp_files_hamburg'  
      externalId: 'sharepointABC_my_file.pdf'  
      name: 'my_file.pdf'  
      description: 'This is a file uploaded from SharePoint.'  
    - space: 'sp_files_hamburg'  
      externalId: 'sharepointABC_my_other_file.pdf'  
      name: 'my_other_file.pdf'  
      description: 'This is another file uploaded from SharePoint.'  
    

### Uploading multiple files​

To upload multiple files without specifying the metadata configuration for each file individually, use this template format for the `FileMetadata` configuration file:

files.FileMetadata.yaml
    
    
    - externalId: sharepointABC_$FILENAME  
      dataSetExternalId: ds_files_hamburg  
      name: $FILENAME  
      source: sharepointABC  
    

or for the `CogniteFile` configuration file:

files.CogniteFile.yaml
    
    
    - space: 'sp_files_hamburg'  
      externalId: sharepointABC_$FILENAME  
      name: $FILENAME  
      description: 'This is a file uploaded from SharePoint.'  
    

This template is recognized by the Cognite Toolkit by

  * It is a YAML file given in `list/array` format.
  * There is a single entry in the list.
  * The `externalId` contains the `$FILENAME` variable.



All files will be uploaded with the same properties except for the `externalId` and `name` properties. The `$FILENAME` variable will be replaced with the filename of the file being uploaded.

## Functions​

**Resource directory _functions/_**

**API documentation:** [Functions](https://developer.cognite.com/api#tag/Functions/operation/postFunctions)

The function configuration files are stored in the module's _functions/_ directory. You can define one or more functions in a single or multiple YAML file(s). The Cognite Toolkit creates the functions in the order they are defined in the file. Functions files must end with `Function`, for example, `my_function.Function.yaml`.

note

The functions YAML files must be located in the _functions/_ directory and not in subdirectories. This allows you to store YAML files that are not configuration files in subdirectories as part of the function's code.

Place the function code and files to deploy to CDF as a function in a subdirectory with the same name as the `externalId` of the function.

**Example function configuration:**

Folder structure, including a function schedule:
    
    
    ./functions/  
             ├── my_function.yaml  
             ├── schedules.yaml  
             └── fn_example_repeater/  
    

Configuration file:

my_functions.Function.yaml
    
    
    # The directory with the function code must have the same name  
    # and externalId as the function itself as defined below.  
    - name: 'example:repeater'  
      externalId: 'fn_example_repeater'  
      owner: 'Anonymous'  
      description: 'Returns the input data, secrets, and function info.'  
      metadata:  
        version: '{{version}}'  
      secrets:  
        mysecret: '{{example_secret}}'  
      envVars:  
        # The two environment variables below are set by the Toolkit  
        ENV_TYPE: '${CDF_BUILD_TYPE}'  
        CDF_ENV: '${CDF_ENVIRON}'  
      runtime: 'py311'  
      functionPath: './src/handler.py'  
      # Data set id for the zip file with the code that is uploaded.  
      dataSetExternalId: 'ds_files_{{default_location}}'  
    

The `functionPath` is the path to the _handler.py_ in the function code directory. In this case, _handler.py_ is expected to be in the _fn_example_repeater/src/_ directory.

Note that `dataSetExternalId` is used to reference the data set that the function itself is assigned to. The Cognite Toolkit automatically resolves the external ID to the internal ID of the data set.

### Function schedules​

**Resource directory:_functions/_**

**API documentation:** [Schedules](https://developer.cognite.com/api#tag/Function-schedules/operation/postFunctionSchedules)

Schedules for functions are also stored in the module's _functions/_ directory. The Cognite Toolkit expects the YAML filename to end with `Schedule`, for example, _run_calculation_x.Schedule.yaml_. You can specify more than one schedule in a single file.

To ensure that the function exists before the schedule is created, schedules are deployed after functions Schedules don't have `externalId`s, and the Cognite Toolkit identifies the schedule by a combination of the `functionExternalId` and the `name`. Consequently, **you can't deploy two schedules for a function with the exact same name** , and with two different sets of data.

daily.Schedule.yaml
    
    
    - name: 'daily-8am-utc'  
      functionExternalId: 'fn_example_repeater'  
      description: 'Run every day at 8am UTC'  
      cronExpression: '0 8 * * *'  
      data:  
        breakfast: 'today: peanut butter sandwich and coffee'  
        lunch: 'today: greek salad and water'  
        dinner: 'today: steak and red wine'  
      authentication:  
        # Credentials to use to run the function in this schedule.  
        # In this example, we just use the main deploy credentials, so the result is the same, but use a different set of  
        # credentials (env variables) if you want to run the function with different permissions.  
        clientId: { { myfunction_clientId } }  
        clientSecret: { { myfunction_clientSecret } }  
    - name: 'daily-8pm-utc'  
      functionExternalId: 'fn_example_repeater'  
      description: 'Run every day at 8pm UTC'  
      cronExpression: '0 20 * * *'  
      data:  
        breakfast: 'tomorrow: peanut butter sandwich and coffee'  
        lunch: 'tomorrow: greek salad and water'  
        dinner: 'tomorrow: steak and red wine'  
    

The `functionExternalId` must match an existing function or a function deployed by the tool.

For schedules, the `authentication` property is optional but recommended. You can use it to specify credentials for the schedule that are different from the default credentials used by the Cognite Toolkit. We recommend using credentials with the **minimum** required access rights to run the function . If you don't specify the `authentication` property, the Cognite Toolkit uses its own credentials to run the function. This only works if the `config.[env].yaml` has set `validation-type: dev`. If it is set to `prod` or anything else, the Cognite Toolkit will raise an error when trying to deploy the schedule without the `authentication` property.

## Hosted Extractors​

_Requires Cognite Toolkit v0.3.0 or later_

**Resource directory:_hosted_extractors/_**

**Hosted extractor documentation:** [Hosted extractors](/cdf/integration/guides/extraction/hosted_extractors)

The hosted extractors are stored in the module's `hosted_extractors/` directory. A hosted extractor has four types of resources: `Source`, `Destination`, `Job`, and `Mapping`. Each resource type has its suffix in the filename, for example, `my_kafka.Source.yaml`.

When creating, updating, and deleting hosted extractors, the Cognite Toolkit applies changes in the correct order based on the dependencies between the source, destination, job, and mapping versions.

### Source​

**API documentation:** [Hosted extractor source](https://api-docs.cognite.com/20230101-beta/tag/Sources/operation/create_sources)

Below is an example of a source configuration file.

my_mqtt.Source.yaml
    
    
    type: mqtt5  
    externalId: my_mqtt  
    host: mqtt.example.com  
    port: 1883  
    authentication:  
      username: myuser  
      password: ${my_mqtt_password}  
    

### Destination​

**API documentation:** [Hosted extractor destination](https://api-docs.cognite.com/20230101-beta/tag/Destinations/operation/create_destinations)

Below is an example of a destination configuration file.

my_cdf.Destination.yaml
    
    
    externalId: my_cdf  
    credentials:  
      clientId: ${my_cdf_clientId}  
      clientSecret: ${my_cdf_clientSecret}  
    targetDataSetExternalId: ds_files_hamburg  
    

note

The Cognite Toolkit automatically resolves the external ID to the internal ID of the data set.

### Job​

**API documentation:** [Hosted extractor job](https://api-docs.cognite.com/20230101-beta/tag/Jobs/operation/create_jobs)

Below is an example of a job configuration file.

my_mqtt_to_cdf.Job.yaml
    
    
    externalId: my_mqtt_to_cdf  
    sourceId: my_mqtt  
    destinationId: my_cdf  
    format:  
      type: value  
      encoding: utf-16  
      compression: gzip  
    

### Mapping​

**API documentation:** [Hosted extractor mapping](https://api-docs.cognite.com/20230101-beta/tag/Mappings/operation/create_mappings)

Below is an example of a mapping configuration file.

my_mqtt_to_cdf.Mapping.yaml
    
    
    externalId: my_mqtt_to_cdf  
    mapping:  
      expression: '[{  
      "type": "datapoint",  
      "timestamp": to_unix_timestamp(input.timestamp, "%Y-%m-%dT%H:%M:%S"),  
      "value": try_float(input.value, null),  
      "externalId": input.tag  
    }].filter(datapoint => datapoint.value is not null)'  
    input:  
      type: json  
    published: true  
    

For more information about the mapping configuration, see the [Hosted extractor documentation](/cdf/integration/guides/extraction/hosted_extractors/kuiper_concepts).

## Locations​

_Requires Cognite Toolkit v0.3.0 or later_

**Resource directory:_locations/_**

The location filters are stored in the module's _locations/_ directory. You can have one or multiple locations in a single YAML file. The location YAML file name must end with `LocationFilter`, for example, `my.LocationFilter.yaml`.

Location filters work with data modeling or with asset-centric resource types. The below example shows a location filter for data modeling.

example.LocationFilter.yaml
    
    
    externalId: unique-external-id-123  
    name: 'Example location name'  
    description: 'This is a description of the location.'  
    parentExternalId: 'The parent location external ID'  
    dataModels:  
      - externalId: CogniteProcessIndustries  
        space: cdf_idm  
        version: v1  
    instanceSpaces:  
      - instance-space-main  
      - instance-space-secondary  
    dataModelingType: DATA_MODELING_ONLY  
    

Asset-centric location filters apply to assets, time series, events, sequences, and events. You can use a shared filter for all of these:

shared_filter.LocationFilter.yaml
    
    
    externalId: unique-external-id-123  
    name: 'Example location name'  
    parentId: 1  
    description: 'This is a description of the location.'  
    assetCentric:  
      dataSetExternalIds:  
        - ds_data_set_890  
      assetSubtreeIds:  
        - externalId: general-subtree-id-890  
      externalIdPrefix: general-prefix  
    dataModelingType: HYBRID  
    

It's common to use either `dataSetExternalId`, `assetSubtreeId`, or `externalIdPrefix` in the filter. The example below illustrates all the options.

You can also set filters for specific resource types, such as `assets`, `events`, `files`, `timeseries`, and `sequences`:

shared_filter.LocationFilter.yaml
    
    
    externalId: unique-external-id-123  
    name: 'Example location name'  
    parentId: 1  
    description: 'This is a description of the location.'  
    assetCentric:  
      assets:  
        dataSetExternalIds:  
          - ds_data_set_123  
        assetSubtreeIds:  
          - externalId: root-asset  
        externalIdPrefix: asset-prefix  
      events:  
        dataSetExternalIds:  
          - ds_data_set_456  
        assetSubtreeIds:  
          - externalId: event-subtree-id-678  
        externalIdPrefix: event-prefix  
      files:  
        dataSetExternalIds:  
          - ds_data_set_789  
        assetSubtreeIds:  
          - externalId: file-subtree-id-901  
        externalIdPrefix: file-prefix  
      timeseries:  
        dataSetExternalIds:  
          - ds_data_set_234  
        assetSubtreeIds:  
          - externalId: timeseries-subtree-id-234  
        externalIdPrefix: timeseries-prefix  
      sequences:  
        dataSetExternalIds:  
          - ds_data_set_567  
        assetSubtreeIds:  
          - externalId: sequence-subtree-id-567  
        externalIdPrefix: sequence-prefix  
    

note

The location filter API uses an **internal ID** for the `parentId` and `dataSetId`, while the YAML configuration files reference the **external ID** ; `parentExternalid` and `dataSetExternalId`. The Cognite Toolkit resolves the external ID to the internal ID before sending the request to the Cognite API.

## RAW​

**Resource directory:_raw/_**

**API documentation:** [RAW](https://developer.cognite.com/api#tag/Raw/operation/postRows)

The RAW configuration files are stored in the module's _raw/_ directory.

You can have one or more RAW configurations in a single YAML file. For example, multiple tables can be defined in a single file. RAW table configuration filenames must end with `Table`, for example, `my_table.Table.yaml`. Database configuration filenames must end with `Database`, for example, `my_database.Database.yaml`.

raw_tables.Table.yaml
    
    
    - dbName: sap  
      tableName: workorder_mdi2_sap  
    - dbName: sap  
      tableName: workorxder_mdi2_sap2  
    

Or you can define one table per file.

sap_workorder_mdi2_sap.Table.yaml
    
    
    dbName: sap  
    tableName: workorder_mdi2_sap  
    

### Uploading data to RAW tables​

caution

Use the Cognite Toolkit only to upload **example data** , and not as a general solution to ingest data into CDF. However, there are use cases where uploading data to RAW tables can be useful see Use case: Uploading data to RAW tables.

You can upload data to RAW tables. You need to create one YAML file per table you want to upload. The data file can either be a _.csv_ or _.parquet_ file and must be named the same name as the YAML file.

This example configuration creates a RAW database called `asset_hamburg_sap` with a table called `assets` and populates it with data from the _asset_hamburg_sap.csv_ file.

asset_hamburg_sap.Table.yaml
    
    
    dbName: asset_hamburg_sap  
    tableName: assets  
    

asset_hamburg_sap.Table.csv
    
    
    "key","categoryId","sourceDb","parentExternalId","updatedDate","createdDate","externalId","isCriticalLine","description","tag","areaId","isActive"  
    "WMT:48-PAHH-96960","1152","workmate","WMT:48-PT-96960","2015-10-06 12:28:33","2013-05-16 11:50:16","WMT:48-PAHH-96960","false","VRD - PH STG1 COMP WTR MIST RELEASED : PRESSURE ALARM HIGH HIGH","48-PAHH-96960","1004","true"  
    "WMT:48-XV-96960-02","1113","workmate","WMT:48-XV-96960","2015-10-08 08:48:04","2009-06-26 15:36:40","WMT:48-XV-96960-02","false","VRD - PH STG1 COMP WTR MIST WTR RLS","48-XV-96960-02","1004","true"  
    "WMT:23-TAL-96183","1152","workmate","WMT:23-TT-96183","2015-10-06 12:28:32","2013-05-16 11:50:16","WMT:23-TAL-96183","false","VRD - PH 1STSTG COMP OIL TANK HEATER : TEMPERATURE ALARM LOW","23-TAL-96183","1004","true"  
    

tip

If the leftmost column in the CSV file is named `key`, the Cognite Toolkit will use this column as the index column for the table.

#### Use case: Uploading data to RAW tables​

The Cognite Toolkit governs resource configurations, typically **metadata** rather than **data**. For example, a sensor's name, location, type, and the asset it's attached to are metadata, while the actual sensor readings are data.

Metadata is typically available from a source system. You can, for example, use an extraction pipeline to extract and ingest the metadata to CDF.

If the metadata isn't available for extraction from a source system, a potential option is to store the metadata as .csv files and have them version-controlled, for example, in a Git repository. Next, you can use the Cognite Toolkit to deploy the metadata to RAW tables in CDF. Then, you can use Transformations to write the metadata to the correct destination resources. This way, you can track changes to the metadata and use the Git repository as the single source of truth for the metadata.

## Relationships​

_Requires Cognite Toolkit v0.4.0 or later_

**Resource directory:_classic/_**

**API documentation:** [Relationships](https://developer.cognite.com/api#tag/Relationships/operation/createRelationships)

Relationships can be found in the module's `classic/` directory. You can define one or more relationships in a single YAML file. The filename must end with `Relationship`, for example, `my_relationship.Relationship.yaml`.

The Cognite Toolkit ensures that dependent resources are created before the relationships. For example, if you reference an asset or a data set in a relationship, the Cognite Toolkit creates the asset or data set before creating the relationship.

Example relationship definition:

my_relationship.Relationship.yaml
    
    
    externalId: MyRelationship  
    sourceType: asset  
    sourceExternalId: MyAsset  
    targetType: event  
    targetExternalId: MyEvent  
    dataSetExternalId: ds_complete_org  
    confidence: 0.42  
    startTime: 1732959346052  
    endTime: 1732959346052  
    labels:  
    - externalId: my_label  
    - externalId: my_other_label  
    

note

The data set is referenced by the `dataSetExternalId`. The Cognite Toolkit automatically resolves the external ID to the internal ID of the data set.

## Robotics​

_Requires Cognite Toolkit v0.3.0 or later_

**Resource directory:_robotics/_**

**API documentation:** The Robotics API is not yet publicly available.

The Robotics configuration files are stored in the module's _robotics/_ directory. There are multiple types of Robotics resources: `RobotCapability`, `Map`, `Location`, `Frame`, `DataPostProcessing`. You can have one or more resources in a single YAML file, but all resources in the file must be of the same type. Each resource type has its suffix in the filename, for example, `my_robot_capability.RobotCapability.yaml`.

### Robot capabilities​

Below is an example of a RobotCapability configuration file.

my_robot_capability.RobotCapability.yaml
    
    
    name: ptz  
    externalId: ptz  
    method: ptz  
    description: Description of the PTZ camera capability  
    inputSchema:  
      $schema: http://json-schema.org/draft-07/schema#  
      id: robotics/schemas/0.1.0/capabilities/ptz  
      title: PTZ camera capability input  
      type: object  
      properties:  
        method:  
          type: string  
        parameters:  
          type: object  
          properties:  
            tilt:  
              type: number  
              minimum: -90  
              maximum: 90  
            pan:  
              type: number  
              minimum: -180  
              maximum: 180  
            zoom:  
              type: number  
              minimum: 0  
              maximum: 100  
          required:  
            - tilt  
            - pan  
            - zoom  
      required:  
        - method  
        - parameters  
      additionalProperties: false  
    dataHandlingSchema:  
      $schema: http://json-schema.org/draft-07/schema#  
      id: robotics/schemas/0.1.0/data_handling/ptz  
      type: object  
      properties:  
        uploadInstructions:  
          type: object  
          properties:  
            image:  
              type: object  
              properties:  
                method:  
                  const: uploadFile  
                parameters:  
                  type: object  
                  properties:  
                    filenamePrefix:  
                      type: string  
                  required:  
                    - filenamePrefix  
              required:  
                - method  
                - parameters  
              additionalProperties: false  
          additionalProperties: false  
      required:  
        - uploadInstructions  
    

In the above schema, we have:

  * **Required properties** : `name`, `externalId` and `method`.
  * **Optional properties** : `description`, `inputSchema`, `dataHandlingSchema`.
  * `inputSchema` and `dataHandlingSchema` are objects and are not verified by the Cognite Toolkit, they are passed as is to the Robotics API.



### Map​

Below is an example of a Map configuration file.

my_map.Map.yaml
    
    
    name: Robot navigation map  
    externalId: robotMap  
    mapType: POINTCLOUD  
    description: A map of the robot's navigation environment  
    frameExternalId: robotFrame  
    data:  
      filename: map.ply  
      mimeType: application/octet-stream  
    locationExternalId: robotLocation  
    scale: 1.0  
    

In the above schema, we have:

  * **Required properties** : `name`, `externalId`, and `mapType`.
  * **Optional properties** : `description`, `data`, `locationExternalId`, `scale`.
  * `MapType` has allowed values `WAYPOINTMAP`, `THREEDMODEL`, `TWODMAP`, and `POINTCLOUD`
  * `data` is an object that is not verified by the Cognite Toolkit, it is passed as is to the Robotics API.



### Location​

Below is an example of a Location configuration file.

my_location.Location.yaml
    
    
    name: Water treatment plant  
    externalId: waterTreatmentPlant1_Windows_3_11_8  
    description: Original Description  
    

In the above schema, we have:

  * **Required properties** : `name` and `externalId`.
  * **Optional properties** : `description`.



### Frame​

Below is an example of a Frame configuration file.

my_frame.Frame.yaml
    
    
    name: Some coordinate frame  
    externalId: someCoordinateFrame  
    transform:  
      parentFrameExternalId: rootCoordinateFrame  
      translation:  
        x: 0  
        y: 0  
        z: 0  
      orientation:  
        x: 0  
        y: 0  
        z: 0  
        w: 1  
    

In the above schema, we have:

  * **Required properties** : `name` and `externalId`.
  * **Optional properties** : `transform`.
  * In `transform`,
    * **Required properties** : `parentFrameExternalId`, `translation`, `orientation`.
    * **Optional properties** : None.
    * For `translation` and `orientation`, all properties are required.



### Data post-processing​

Below is an example of a DataPostProcessing configuration file.

my_data_post_processing.DataPostProcessing.yaml
    
    
    name: Read dial gauge  
    externalId: read_dial_gauge  
    method: read_dial_gauge  
    description: Original Description  
    inputSchema:  
      $schema: http://json-schema.org/draft-07/schema#  
      id: robotics/schemas/0.1.0/capabilities/ptz  
      title: PTZ camera capability input  
      type: object  
      properties:  
        method:  
          type: string  
        parameters:  
          type: object  
          properties:  
            tilt:  
              type: number  
              minimum: -90  
              maximum: 90  
            pan:  
              type: number  
              minimum: -180  
              maximum: 180  
            zoom:  
              type: number  
              minimum: 0  
              maximum: 100  
          required:  
            - tilt  
            - pan  
            - zoom  
      required:  
        - method  
        - parameters  
      additionalProperties: false  
    

In the above schema, we have:

  * **Required properties** : `name`, `externalId`, and `method`.
  * **Optional properties** : `description`, `inputSchema`.
  * `inputSchema` is an object and is not verified by the Cognite Toolkit, it is passed as is to the Robotics API.



## Sequences​

_Requires Cognite Toolkit v0.3.0 or later_

Sequence rows requires Cognite Toolkit v0.4.0 or later

**Resource directory:_classic/_**

**API documentation:** [Sequences](https://api-docs.cognite.com/20230101/tag/Sequences/operation/createSequence)

**API documentation Rows:** [Sequence Rows](https://api-docs.cognite.com/20230101/tag/Sequences/operation/postSequenceData)

Sequences can be found in the module's `classic/` directory. You can define one or more sequences in a single YAML file. The filename must end with `Sequence`, for example, `my_sequence.Sequence.yaml`.

Below is an example of a sequence configuration file.

my_sequence.Sequence.yaml
    
    
    externalId: windturbine_powercurve_xyz  
    name: Wind turbine power curve XYZ  
    description: A power curve for a wind turbine model XYZ  
    dataSetExternalId: ds_sequences  
    assetExternalId: wind_turbine_xyz  
    metadata:  
      manufacturer: WindTurbineCorp  
      model: XYZ  
    columns:  
      - externalId: wind_speed  
        valueType: DOUBLE  
        description: Wind speed in m/s  
        name: Display name for wind speed  
      - externalId: power  
        valueType: DOUBLE  
        description: Power in kW  
        name: Display name for power  
    

note

The data set is referenced by the `dataSetExternalId`. The Cognite Toolkit automatically resolves the external ID to the internal ID of the data set.

### Sequence rows​

Sequence **rows** are a separate resource type from sequences. The sequence row configuration files are expected in the _classic/_ directory and must have the suffix `SequenceRow`, for example, `my_sequence.SequenceRow.yaml`. Below is an example of a sequence row configuration file.

powercurve.SequenceRow.yaml
    
    
    externalId: SequenceWithRows  
    columns:  
    - wind_speed  
    - power  
    rows:  
    - rowNumber: 1  
      values:  
      - 0.0  
      - 0.0  
    - rowNumber: 2  
      values:  
      - 5.0  
      - 309000.0  
    - rowNumber: 3  
      values:  
      - 10.0  
      - 2693000.0  
    - rowNumber: 4  
      values:  
      - 15.0  
      - 3450000.0  
    - rowNumber: 5  
      values:  
      - 20.0  
      - 3450000.0  
    - rowNumber: 6  
      values:  
      - 25.0  
      - 3450000.0  
    

The `externalId` is the same as the sequence's `externalId`. The `columns` property lists the columns in the sequence. The `rows` property contains the data for the sequence. Each row has a `rowNumber` and a `values` property. The `values` property is an array of values for each column in the sequence.

## Streamlit applications​

_Requires Cognite Toolkit v0.4.0 or later_

**Resource directory:_streamlit/_**

**API documentation:** This uses the files API: [Files](https://developer.cognite.com/api#tag/Files/operation/initFileUpload)

Streamlit applications are stored in the module's _streamlit/_ directory. You can define one or more Streamlit applications in a single YAML file. The filename must end with `Streamlit`, for example, `myapp.Streamlit.yaml`.

Below is an example of a Streamlit application configuration file.

myapp.Streamlit.yaml
    
    
    externalId: myapp  
    name: MySuperApp  
    creator: doctrino@github.com  
    description: This is a super app  
    published: true  
    theme: Light  
    thumbnail: 'data:image/webp;base64,....'  
    dataSetExternalId: ds_complete_org  
    entrypoint: main.py  
    

note

The data set is referenced by the `dataSetExternalId`. The Cognite Toolkit automatically resolves the external ID to the internal ID of the data set.

The `externalId` of the application must be unique within the project and must match the name of a directory where the `.py` files are located, including the `entrypoint` file. In addition, there must be a `requirements.txt` file in the same directory. For the above example, the directory structure would look like this:
    
    
    ./<my_module>  
       └── streamlit/  
            ├── myapp.Streamlit.yaml  
            └── myapp/  
                ├── main.py  
                └── requirements.txt  
    

## Transformations​

**Resource directory:_transformations/_**

Transformation Notifications requires Cognite Toolkit v0.3.0 or later

**API documentation Transformations:** [Transformations](https://developer.cognite.com/api#tag/Transformations/operation/createTransformations)

**API documentation Schedules:** [Schedule](https://api-docs.cognite.com/20230101/tag/Transformation-Schedules/operation/createTransformationSchedules)

**API documentation Notifications:** [Notifications](https://api-docs.cognite.com/20230101/tag/Transformation-Notifications/operation/createTransformationNotifications)

The transformation configuration files are stored in the module's _transformations/_ directory. You can have one or more transformations in a single YAML file, but typically you have one transformation per file. The filename must end with `Transformation`, for example, `my_transformation.Transformation.yaml`.

Each transformation can have a corresponding _.sql_ file with the accompanying SQL code. The _.sql_ file should have the same filename as the YAML file that defines the transformation (without the number prefix) or use the _externalId_ of the transformation as the filename.

The transformation schedule is a separate resource type, tied to the transformation by `external_id`.

The Cognite Toolkit detects the transformation schedule YAML file by the `schedule` suffix in the filename, for example, `my_transformation.schedule.yaml`. The transformation notification YAML file is detected by the `Notification` suffix in the filename, for example, `my_transformation.Notification.yaml`. All other YAML files are considered transformation configurations.

### Transformation configuration​

**Example transformation configuration:**

tr_asset_oid_workmate_asset_hierarchy.Transformation.yaml
    
    
    externalId: 'tr_asset_{{location_name}}_{{source_name}}_asset_hierarchy'  
    dataSetExternalId: 'ds_asset_{{location_name}}'  
    name: 'asset:{{location_name}}:{{source_name}}:asset_hierarchy'  
    destination:  
      type: 'asset_hierarchy'  
    ignoreNullFields: true  
    isPublic: true  
    conflictMode: upsert  
    tags:  
    - 'asset_hierarchy'   
    # Specify credentials separately like this:  
    # You can also use different credentials for running the transformations than the credentials you use to deploy.  
    authentication:  
      clientId: { { cicd_clientId } }  
      clientSecret: { { cicd_clientSecret } }  
      tokenUri: { { cicd_tokenUri } }  
      # Optional: If idP requires providing the cicd_scopes  
      cdfProjectName: { { cdfProjectName } }  
      scopes: { { cicd_scopes } }  
      # Optional: If idP requires providing the cicd_audience  
      audience: { { cicd_audience } }  
    

tr_asset_oid_workmate_asset_hierarchy.Transformation.sql
    
    
    SELECT  
      externalId                      as externalId,  
      if(parentExternalId is null,  
         '',  
         parentExternalId)            as parentExternalId,  
      tag                             as name,  
      sourceDb                        as source,  
      description,  
      dataset_id('{{asset_dataset}}')     as dataSetId,  
      to_metadata_except(  
        array("sourceDb", "parentExternalId", "description"), *)  
                                      as metadata  
    FROM  
      `{{asset_raw_input_db}}`.`{{asset_raw_input_table}}`  
      
    

You can configure the transformation with both **from** and **to** sets of credentials. Use the `authentication` section to specify the credentials. See below for more information on how to configure the credentials.

You can specify the SQL inline in the transformation YAML file, using the `query` property (str), but we recommend that you use a separate _.sql_ file for readability.

In the above transformation, the transformation re-uses the globally defined credentials for the Cognite Toolkit. For production projects, we recommend that you use a service account with the **minimum** required access rights instead.

### Transformation credentials​

You can specify the credentials in the `authentication` section of the transformation YAML file. The most common way is as follows:
    
    
    ...  
    authentication:  
      clientId: my_client_id  
      clientSecret: my_client_secret  
    

Here, `clientId` and `clientSecret` are used to authenticate against a service principal that is connected to a Cognite group with the capabilities (authorization) needed to run the transformation. The service principal must be authorized to read from the source table and write to the transformation destination, for example, a data model.

You can also specify two sets of credentials, one for reading from the source and one for writing to the destination.
    
    
    ...  
    authentication:  
      read:  
        clientId: read_service_principle_client_id  
        clientSecret: read_service_principle_client_secret  
      write:  
        clientId: destination_service_principle_client_id  
        clientSecret: destination_service_principle_client_secret  
    

In this case, the `read` credentials are used to read from the source table, and the `write` credentials are used to write to the destination.

If you need to authenticate against a different CDF project, you can specify full credentials:
    
    
    authentication:  
      clientId: my_client_id  
      clientSecret: my_client_secret  
      tokenUri: https://cognite.com/oauth/token  
      cdfProjectName: my_cdf_project_name  
      scopes: ['https://cognite.com/.default']  
      audience: 'https://cognite.com'  
    

or full credentials for both reading and writing:
    
    
    authentication:  
      read:  
        clientId: read_service_principle_client_id  
        clientSecret: read_service_principle_client_secret  
        tokenUri: https://cognite.com/oauth/token  
        cdfProjectName: my_cdf_project_name  
        scopes: ['https://cognite.com/.default']  
        audience: 'https://cognite.com'  
      write:  
        clientId: destination_service_principle_client_id  
        clientSecret: destination_service_principle_client_secret  
        tokenUri: https://cognite.com/oauth/token  
        cdfProjectName: my_cdf_project_name  
        scopes: ['https://cognite.com/.default']  
        audience: 'https://cognite.com'  
    

The most common use case for this is to read from one CDF project and write to another CDF project.

### Transformation Schedule​

The transformation `schedule` is optional. If you do not specify a schedule, the transformation will be created, but not scheduled. You can then schedule it manually in the CDF UI or using the Cognite API. Schedule is a separate API endpoint in CDF.

**Example transformation schedule configuration:**

tr_asset_oid_workmate_asset_hierarchy.schedule.yaml
    
    
    externalId: 'tr_asset_{{location_name}}_{{source_name}}_asset_hierarchy'  
    interval: '{{scheduleHourly}}'  
    isPaused: {{ pause_transformations }}  
    

### Transformation Notifications​

The transformation `notification` is optional. Below is an example of a transformation notification configuration file.

tr_notifications.Notification.yaml
    
    
    - transformationExternalId: tr_first_transformation  
      destination: john.smith@example.com  
    - transformationExternalId: tr_first_transformation  
      destination: jane.smith@example.com  
    

caution

CDF identifies notifications by their **internal ID** while the Cognite Toolkit uses a combination of the **transformation external ID** and the **destination** to identify each notification Running `cdf clean` deletes **all** notifications for a transformation external ID and destination.

## Time series​

**Resource directory:_timeseries/_**

**API documentation:** [Time-series](https://developer.cognite.com/api#tag/Time-series/operation/postTimeSeries)

caution

Use the Cognite Toolkit only to upload **example data** , and not as a general solution to ingest time series into CDF.

TimeSeries can be found in the module's `timeseries/` directory. You can define the metadata of one or more time series in a single or multiple YAML file(s). The filename must end with `TimeSeries`, for example, `my_timeseries.TimeSeries.yaml`.

note

Typically, you create time series when ingesting data into CDF by configuring the data pipelines with the corresponding data sets, databases, groups, and so on.

Example time series configuration:

timeseries.TimeSeries.yaml
    
    
    - externalId: 'pi_160696'  
      name: 'VAL_23-PT-92504:X.Value'  
      dataSetExternalId: ds_timeseries_hamburg  
      isString: false  
      metadata:  
        compdev: '0'  
        location5: '2'  
        pointtype: Float32  
        convers: '1'  
        descriptor: PH 1stStgSuctCool Gas Out  
        contextMatchString: 23-PT-92504  
        contextClass: VAL  
        digitalset: ''  
        zero: '0'  
        filtercode: '0'  
        compdevpercent: '0'  
        compressing: '0'  
        tag: 'VAL_23-PT-92504:X.Value'  
      isStep: false  
      description: PH 1stStgSuctCool Gas Out  
      assetExternalId: '23-PT-92504'  
    - externalId: 'pi_160702'  
      name: 'VAL_23-PT-92536:X.Value'  
      dataSetExternalId: ds_timeseries_hamburg  
      isString: false  
      metadata:  
        compdev: '0'  
        location5: '2'  
        pointtype: Float32  
        convers: '1'  
        descriptor: PH 1stStgComp Discharge  
        contextMatchString: 23-PT-92536  
        contextClass: VAL  
        digitalset: ''  
        zero: '0'  
        filtercode: '0'  
        compdevpercent: '0'  
        compressing: '0'  
        tag: 'VAL_23-PT-92536:X.Value'  
    

This configuration creates two timeseries in the `ds_timeseries_hamburg` data set with the external IDs `pi_160696` and `pi_160702`.

### Uploading datapoints to time series​

caution

Use the Cognite Toolkit only to upload **example data** , and not as a general solution to ingest time series into CDF.

You can upload datapoints to times series using the Cognite Toolkit. The datapoints are stored in the module's _timeseries/_ directory. Datapoints are stored in `csv` or `parquet` files. There is no requirements for the filename of the datapoints file.

note

Typically, you create time series when ingesting data into CDF by configuring the data pipelines with the corresponding data sets, databases, groups, and so on.

Example of datapoints:

datapoints.csv
    
    
    timestamp,pi_160696,pi_160702  
    2013-01-01 00:00:00,0.9430412044195982,0.9212588490581821  
    2013-01-01 01:00:00,0.9411303320132799,0.9212528389403117  
    2013-01-01 02:00:00,0.9394743147709556,0.9212779911470234  
    2013-01-01 03:00:00,0.9375842300608798,  
    2013-01-01 04:00:00,0.9355836846172971,0.9153202184209938  
    

This _.csv_ file loads data into the time series created in the previous example. The first column is the timestamp, and the following columns are the external ID for the time series at that timestamp.

## Timeseries subscriptions​

_Requires Cognite Toolkit v0.2.0 or later_

**Resource directory:_timeseries_ /**

**API documentation:** [Timeseries subscriptions](https://developer.cognite.com/api#tag/Data-point-subscriptions)

Timeseries subscriptions are stored in the module's _timeseries/_ directory. We recommend to have a separate YAML file for each subscription. Use the `DatapointSubscription` suffix in the filename, for example `my_subscription.DatapointSubscription.yaml`.

The Cognite Toolkit create the timeseries subscription after the timeseries.

Example timeseries subscription configuration:

my_subscription.DatapointSubscription.yaml
    
    
    externalId: my_subscription  
    name: My Subscription  
    description: All timeseries with externalId starting with ts_value  
    partitionCount: 1  
    dataSetExternalId: ds_timeseries_hamburg  
    filter:  
      prefix:  
        property:  
          - externalId  
        value: ts_value  
    

## Workflows​

_Requires Cognite Toolkit v0.2.0 or later_

WorkflowTrigger requires Cognite Toolkit v0.3.0 or later

**Resource directory:_workflows/_**

**API documentation:** [Workflows](https://developer.cognite.com/api/#tag/Workflows)

The workflows are stored in the module's `workflows/` directory. A workflow has three types of resources: `Workflow`, `WorkflowVersion`, and `WorkflowTrigger`. They are identified by the `Workflow.yaml`, `WorkflowVersion.yaml`, and `WorkflowTrigger` suffixes. We recommend having one file per workflow and workflow version.

When creating, updating, and deleting workflows, the Cognite Toolkit applies changes in the correct order based on the dependencies between the workflows and workflow versions. The Cognite Toolkit creates transformations and functions before the workflow versions to ensure that the workflow versions can reference them.

Example workflow:

my_workflow.Workflow.yaml
    
    
    externalId: wf_my_workflow  
    description: A workflow for processing data  
    dataSetExternalId: ds_workflow_data  
    

Example workflow version:

my_version.WorkflowVersion.yaml
    
    
    workflowExternalId: wf_my_workflow  
    version: '1'  
    workflowDefinition:  
      description: 'Run tasks in sequence'  
      tasks:  
        - externalId: '{{ workflow_external_id }}_function_task'  
          type: 'function'  
          parameters:  
            function:  
              externalId: 'fn_first_function'  
              data: {}  
            isAsyncComplete: false  
          name: 'Task One'  
          description: First task  
          retries: 3  
          timeout: 3600  
          onFailure: 'abortWorkflow'  
        - externalId: '{{ workflow_external_id }}_transformation_task'  
          type: 'transformation'  
          parameters:  
            transformation:  
              externalId: 'tr_first_transformation'  
              concurrencyPolicy: fail  
          name: 'Task Two'  
          description: Second task  
          retries: 3  
          timeout: 3600  
          onFailure: 'skipTask'  
          dependsOn:  
            - externalId: '{{ workflow_external_id }}_function_task'  
    

Example workflow trigger:

my_trigger.WorkflowTrigger.yaml
    
    
    externalId: my_trigger  
    triggerRule:  
      triggerType: schedule  
      cronExpression: '0 0 * * *'  
    input:  
      my_input: 'data'  
    metadata:  
      origin: cognite-toolkit  
    workflowExternalId: wf_my_workflow  
    workflowVersion: '1'  
    authentication:  
      clientId: {{ my_trigger_clientId }}  
      clientSecret: ${IDP_WF_TRIGGER_SECRET}  
    

tip

You can specify the credentials for the workflow trigger by adding a `authentication` property to the `WorkflowTrigger` configuration.
    
    
    externalId: my_trigger  
    ---  
    authentication:  
      clientId: { { my_trigger_clientId } }  
      clientSecret: ${IDP_WF_TRIGGER_SECRET}  
    

caution

The Cognite API doesn't support updating workflow Triggers. When you update a trigger with the Cognite Toolkit, the Cognite Toolkit deletes the existing trigger and creates a new one with the updated configuration. This means that the run history of the trigger is lost.

Last updated: September 7, 2025

  * 3D Models
  * Agents
    * Available tools
  * Assets
    * Table formats
  * Groups
    * Groups and group deletion
    * ACL scoping
  * Security categories
  * Data models
    * Spaces
    * Containers
    * Views
    * Data models
    * Nodes
    * Edges
  * Data sets
  * Events
  * InfieldV1
  * Labels
  * Extraction pipelines
  * Files
    * Uploading multiple files
  * Functions
    * Function schedules
  * Hosted Extractors
    * Source
    * Destination
    * Job
    * Mapping
  * Locations
  * RAW
    * Uploading data to RAW tables
  * Relationships
  * Robotics
    * Robot capabilities
    * Map
    * Location
    * Frame
    * Data post-processing
  * Sequences
    * Sequence rows
  * Streamlit applications
  * Transformations
    * Transformation configuration
    * Transformation credentials
    * Transformation Schedule
    * Transformation Notifications
  * Time series
    * Uploading datapoints to time series
  * Timeseries subscriptions
  * Workflows



E-learning

  * [Cognite Academy](https://learn.cognite.com/)



Community

  * [Cognite Hub](https://hub.cognite.com/)



Support

  * [Cognite Support](https://cognite.zendesk.com/hc/en-us)



Legal

  * [Terms and conditions](https://www.cognite.com/en/generalterms)



![](/images/logos/cogfooter.svg)![](/images/logos/cogfooter.svg)
