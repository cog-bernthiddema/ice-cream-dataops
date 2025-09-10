Write SQL queries | Cognite Documentation

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

  * [Deutsch](/de/cdf/integration/guides/transformation/write_sql_queries)
  * [English](/cdf/integration/guides/transformation/write_sql_queries)
  * [Français](/fr/cdf/integration/guides/transformation/write_sql_queries)
  * [Español](/es/cdf/integration/guides/transformation/write_sql_queries)
  * [Italiano](/it/cdf/integration/guides/transformation/write_sql_queries)
  * [Latviešu](/lv/cdf/integration/guides/transformation/write_sql_queries)
  * [Nederlands](/nl/cdf/integration/guides/transformation/write_sql_queries)
  * [Norsk](/no/cdf/integration/guides/transformation/write_sql_queries)
  * [Português](/pt/cdf/integration/guides/transformation/write_sql_queries)
  * [Română](/ro/cdf/integration/guides/transformation/write_sql_queries)
  * [Svenska](/sv/cdf/integration/guides/transformation/write_sql_queries)
  * [한국어](/ko/cdf/integration/guides/transformation/write_sql_queries)
  * [中文](/zh/cdf/integration/guides/transformation/write_sql_queries)
  * [日本語](/ja/cdf/integration/guides/transformation/write_sql_queries)



![](https://cognite-federatedsearch.azurewebsites.net/appbar/app.png)

[![](https://cognite-federatedsearch.azurewebsites.net/appbar/ask.png) Cognite Hub ![](https://cognite-federatedsearch.azurewebsites.net/appbar/open.png)](https://hub.cognite.com/)[![](https://cognite-federatedsearch.azurewebsites.net/appbar/academy.png) Cognite Academy ![](https://cognite-federatedsearch.azurewebsites.net/appbar/open.png)](https://learn.cognite.com/)[![](https://cognite-federatedsearch.azurewebsites.net/appbar/statuspage.png) Cognite status page ![](https://cognite-federatedsearch.azurewebsites.net/appbar/open.png)](https://status.cognite.com/)[![](https://cognite-federatedsearch.azurewebsites.net/appbar/support.png) Cognite support ![](https://cognite-federatedsearch.azurewebsites.net/appbar/open.png)](https://cognite.zendesk.com/hc/en-us/requests/new)

###### Cognite website

[www.cognite.com![](https://cognite-federatedsearch.azurewebsites.net/appbar/open.png)](https://www.cognite.com/)

  * [About data engineering](/cdf/data_engineering/)

    * [Explore data](/cdf/integration/concepts/exploration/)

    * [Data governance](/cdf/data_governance/)

    * [Data modeling](/cdf/dm/)

    * [Data workflows](/cdf/data_workflows/)

    * [Integrate data](/cdf/integration/)

    * [Staging](/cdf/integration/guides/extraction/raw_explorer)
    * [Transform data](/cdf/integration/concepts/transformation/)

      * [Setup and administration](/cdf/integration/guides/transformation/admin_oidc)
      * [Transformations](/cdf/integration/guides/transformation/transformations)

        * [Write SQL queries](/cdf/integration/guides/transformation/write_sql_queries)
      * [Transformations CLI](/cdf/integration/guides/transformation/transformations_cli)
    * [Contextualize data](/cdf/integration/concepts/contextualization/)

    * [Build solutions](/cdf/concepts/build)




On this page

# Write SQL queries

Transform data from the CDF staging area into a data model using built-in and custom Spark SQL queries. Select **Switch to SQL editor** on the **Transform data** page to create a transformation in Spark SQL. This article describes the queries and explains how you can load data incrementally.

Tip

The SQL editor offers built-in code completion and [built-in Spark SQL functions](https://archive.apache.org/dist/spark/docs/3.3.4/api/sql/index.html) and Cognite custom SQL functions.

Note

Your changes won't be kept if you switch from the SQL editor to the mapping editor.

## Read from a CDF staging table​

To select data from a CDF staging table, use the syntax `mydb.mytable`:
    
    
    select  
     *  
    from  
     database-name.table-name  
    

If your database or table name contains special characters, enclose the name in backticks, for example ``my-db`.`my table``.

### Avoid schema inference​

Transformations infer schemas in the CDF staging table, but this process only uses a subset of all the rows in the table. You can avoid schema inference and write a schema fitted your data.

To avoid schema inference:
    
    
      select  
       *  
      from  
       cdf_raw("database-name", "table-name")  
    

This returns data with the schema `key:STRING`, `lastUpdatedTime:TIMESTAMP`, `columns:STRING`, where the `columns` string contains the JSON value encoded as a string.

Here's an example of how to enforce a user-defined schema:
    
    
        select  
      
         get_json_object(columns, '$.externalId') AS externalId,  
      
         timestamp(get_json_object(columns, '$.timestamp')) AS timestamp,  
      
         double(get_json_object(columns, '$.value')) AS value  
      
        from  
         cdf_raw("database-name", "table-name")  
    

## Read from a CDF file​

To read data from a file uploaded to the CDF Files API, use the syntax below:
    
    
      select * from cdf_file_content("file-external-id")  
    

The file must fulfill the following requirements:

  * Format must be [`JSON Lines`](https://jsonlines.org/) (also called `NDJSON`).
  * Size must be below 5GB.
  * File must be `utf-8` encoded.



note

Duplicate rows in the file are removed when processed by Transformations.

### Avoid schema inference​

To avoid schema inference, use the optional `schema-inference` parameter (set to `true` by default):
    
    
      select * from cdf_file_content("file-external-id", false)  
    

The query returns the data with the schema `value: STRING`, where the `value` string contains the JSON value encoded as a string.

For example, use the user-defined schema below:
    
    
        select  
      
          get_json_object(value, '$.externalId') AS externalId,  
      
          timestamp(get_json_object(value, '$.timestamp')) AS timestamp,  
      
          double(get_json_object(value, '$.value')) AS value  
      
        from  
          cdf_file_content("file-external-id", false)  
    

## Read from other CDF resource types​

To select other CDF resource types, use the syntax `_cdf.resource_type`.
    
    
    select * from _cdf.events  
    

The supported resource types are:

  * `_cdf.events`
  * `_cdf.assets`
  * `_cdf.files`
  * `_cdf.timeseries`
  * `_cdf.sequences`
  * `_cdf_sequences.<sequence_externalId>`
  * `_cdf.datapoints`
  * `_cdf.stringdatapoints`
  * `_cdf.labels`
  * `_cdf.relationships`



## Load data incrementally​

When reading data, your transformation jobs will run much faster and more efficiently if it only has to read the data that has changed since the last time the transformation job ran. This reduces the time to run a transformation, and allows for more frequent runs. One way to achieve this, is to filter on the `lastUpdatedTime` column to query for the rows that have changed after a specific timestamp. The filter on `lastUpdatedTime` is pushed to the underlying resource type (if supported) to run the query more efficiently and only return changes.

There are some minor syntax differences between some of the resource types for this filtering, but for example, when reading from [staging](https://api-docs.cognite.com/20230101/tag/Raw) tables it could look like this:

`select * from mydb.mytable where lastUpdatedTime > to_timestamp(123456)`.

Instead of encoding the timestamp in the query and keeping it up to date every time new data has been processed, you can use the `is_new` function to do this for you automatically. The function returns `true` when a row has changed since the last time the transformation was run and `false` otherwise. This filters out older rows before the results are processed.

The **first** time you run a transformation using the query below, all the rows of `mytable` will be processed:
    
    
    select * from mydb.mytable where is_new("mydb_mytable", lastUpdatedTime)  
    

If the transformation completes successfully, the **second** run will only process rows that have changed since the first run.

If the transformation fails, `is_new` filters the same rows the next time the transformation is run. This ensures that there is no data loss in the transformation from source to destination.

note

Incremental load is disabled when previewing query results. That is, `is_new` will always return `true` for all rows.

Each `is_new` filter is identified by a name and can be set to any constant string (for example,`"mydb_mytable"` in the above example). This allows you to differentiate between multiple calls to `is_new` in the same query and use `is_new` to filter on multiple tables. To easily identify the different filters, we recommend that you use the name of the table as the name of the `is_new` filter. The name is stored with the transformation and must be unique for the specific transformation. If you use the same name in two different transformations, they're stored separately to not interfere with each other.

note

It's not common to use multiple `is_new` filters in the same query. Instead, it's more likely you'll use `is_new` on the main resource you're accessing. Then, you can join in different resources with data to improve any new entries from the main table or resource. If you use multiple `is_new` filters, they are applied to each source separately before any join operations are evaluated. This means that for the `join` to work correctly in this case, both sources have to be updated at the same time.

### Resource types supporting incremental data loading on the `lastUpdatedTime` column​

Incremental data loading is supported by filtering on `lastUpdatedTime` for the following resource types in addition to [staging](https://api-docs.cognite.com/20230101/tag/Raw):

  * `_cdf.assets`
  * `_cdf.events`
  * `_cdf.files`
  * `_cdf.timeseries`
  * `_cdf.relationships`
  * `_cdf.datasets`



### Incremental data loading when using Data Modeling​

For data modeling, we don't recommend filtering on `timestamp` or `int64` columns. Instead, it is more efficient to use the variant of the `is_new` function that uses the [sync](/cdf/dm/dm_concepts/dm_querying#syncing---subscribing-to-changes) API to read all changes since the last time the transformation was successfully run. This `is_new` function is used when it references the `cdf_nodes()`, `cdf_edges()` or `cdf_data_models()` functions instead of a single column like `lastUpdatedTime`.

This could look like this:
    
    
    select * from cdf_nodes() where is_new('my_nodes')  
    

where `is_new` will filter on the output of `cdf_nodes`.

Each `is_new` filter is identified by a name and can be set to any constant string (for example,`"my_nodes"` in the above example).

If you have multiple sources in the same query, you must specify which source the `is_new` is referencing. This is done by providing an alias on the source function, like this:
    
    
    select * from cdf_nodes() a, cdf_edges() b where is_new('a_nodes', a)  
    

Here the query defines an alias for the `cdf_nodes()` function, and then specifies to apply the `is_new` filter on this alias. This is different than how `is_new` is used for other resource types, where the specification is to a specific column in the source.

The source can be any of the `cdf_nodes`, `cdf_edges` or `cdf_data_models` functions, and can reference a specific view, such as:
    
    
    select * from cdf_data_models('space', 'datamodel_external_id', 'version', 'view') where is_new('datamodel_view')  
    

`is_new` translates the query to filter on a cursor that tracks all changes. The cursor is updated every time the transformation is successfully run, in the same way as `is_new` for other resource types. You don't need to explicitly model support for this filtering in your data model, as it is inherently supported in [data modeling](/cdf/dm/). You can also combine this with other filters (where clauses), and it will use any matching indexes set up in data modeling to ensure performance of any optional filters.

Warning

When using `is_new` with data modeling, the transformation must run at least once per three days to ensure it can find the difference between the last run and the new run. If it doesn't run for three days or more, the transformation falls back to read all of the input data.

## Backfill​

To process all the data even if it hasn't changed since the last transformation, change the name of the `is_new` filter, for example, by adding a postfix with an incrementing number (e.g. `"mydb_mytable_1"`).

This is especially useful when the logic of the query changes and data that has already been imported needs to be updated accordingly.

## Write to specific properties in data modeling​

In data modeling, a [type node](/cdf/dm/dm_concepts/dm_spaces_instances#type-nodes) can represent anything from physical entities to abstract concepts like a comment or the type of a physical entity. Every instance (nodes and edges) in data modeling has a type property. This property is a direct relation pointing to the node that defines its intended type.

To populate the **type** attribute for instances, use the **_type** keyword in your transformation SQL statement.

The example below uses the `_type` column to read, write, and filter instances.
    
    
    select  
      cast(`externalId` as STRING) as externalId,  
      node_reference("typeSpace", "newTypeNodeExtId") as _type,  
      _type as previousType,  
      cast(`name` as STRING) as name  
    from  
      cdf_data_models("spaceExtId", "model", "1", "Facility")  
    where   
      _type = node_reference("typeSpace", "oldTypeNodeExtId")  
    

The `_type` is a property of the instance and isn't associated with any view. You can name a view property "type", and it can be referenced using the `type` keyword.

For more information, see [Type nodes in data modeling](/cdf/dm/dm_concepts/dm_spaces_instances#type-nodes).

## Custom SQL functions​

In addition to the built-in [Spark SQL functions](https://spark.apache.org/docs/latest/api/sql/index.html), we also provide a set of custom SQL functions to help you write efficient transformations.

note

When a function expects `var_args`, it allows a variable number of arguments of any type, including star `*`.

### get_names​

  * **get_names(var_args): Array[String]**



Returns an array of the field names of a struct or row.

**Example**
    
    
    select get_names(*) from mydb.mytable  
    -- Returns the column names of 'mydb.mytable'  
    
    
    
    select get_names(some_struct.*) from mydb.mytable  
    -- Returns the field names of 'some_struct'  
    

### cast_to_strings​

  * **cast_to_strings(var_args): Array[String]**



Casts the arguments to an array of strings. It handles array, struct and map types by casting it to JSON strings.

**Example**
    
    
    select cast_to_strings(*) from mydb.mytable  
    -- Returns the values of all columns in 'mydb.mytable' as strings  
    

### to_metadata​

  * **to_metadata(var_args): Map[String, String]**



Creates metadata compatible type from the arguments. In practice it does `map_from_arrays(get_names(var_args), cast_to_strings(var_args))`. Use this function when you want to transform your columns or structures into a format that fits the metadata field in CDF.

**Example**
    
    
    select to_metadata(*) from mydb.mytable  
    -- Creates a metadata structure from all the columns found in 'mydb.mytable'  
    

### to_metadata_except​

  * **to_metadata_except(excludeFilter: Array[String], var_args)**



Returns a metadata structure (`Map[String, String]`) where strings found in `excludeFilter` will exclude keys from `var_args`.

Use this function when you want to put most, but not all, columns into metadata, for example `to_metadata_except(array("someColumnToExclude"), *)`

**Example**
    
    
    select to_metadata_except(array("myCol"), myCol, testCol) from mydb.mytable  
    -- Creates a map where myCol is filtered out.  
    -- The result in this case will be Map("testCol" -> testCol.value.toString)  
    

### asset_ids​

Attempts to find asset names under the given criteria and return the IDs of the matching assets. Three variations are available.

Attempts to find given `assetNames` in all assets.

  * **asset_ids(assetNames: Array[String]): Array[BigInt]**



Attempts to find `assetNames` in the asset hierarchy with `rootAssetName` as their root asset.

  * **asset_ids(assetNames: Array[String], rootAssetName: String): Array[BigInt]**



Attempts to find `assetNames` that belong to the `datasetIds`.

  * **asset_ids(assetNames: Array[String], datasetIds: Array[Long]): Array[BigInt]**



Attempts to find `assetNames` that belong to the `datasetIds` under the `rootAssetName`.

  * **asset_ids(assetNames: Array[String], rootAssetName: String, datasetIds: Array[Long]): Array[BigInt]**



See [Assets](https://developer.cognite.com/dev/concepts/resource_types/assets) for more information about assets in CDF.

important

The entire job will be aborted if `asset_ids()` did not find any matching assets.

**Example**
    
    
    select asset_ids(array("PV10", "PV11"))  
    select asset_ids(array("PV10", "PV11"), "MyBoat")  
    select asset_ids(array("PV10", "PV11"), array(254343, 23433, 54343))  
    select asset_ids(array("PV10", "PV11"), array(dataset_id("pv-254343-ext-id"), 23433, 54343))  
    select asset_ids(array("PV10", "PV11"), "MyBoat", array(dataset_id("pv-254343-ext-id"), 23433, 54343))  
    

### is_new​

  * **is_new(name: String, version: long)**



Returns `true` if the version provided is higher than the version found with the specified name, based on the last time the transformation was run. version can be any column of dataype `long` with only incremental values ingested. A popular example is the `lastUpdatedTime` column.

  * If the transformation completes successfully, the next transformation job only processes rows that have changed since the start of the last successfully completed transformation job.

  * If the transformation fails, `is_new` processes all rows that have changed since the start of the last successful run. This ensures no data loss in the transformation from source to destination. See also Load data incrementally.




Tip

If you're using more than one occurrence of `is_new()` in one transformation, we recommend that you use different variable names. This guarantees that subqueries within one transformation don't override the `lastUpdatedTime` record before the transformation is completed.

**Example**
    
    
    select * from mydb.mytable where is_new("mydb_mytable_version", lastUpdatedTime)  
    -- Returns only rows that have changed since the last successful run  
    

### dataset_id​

  * **dataset_id(externalId: String): BigInt**



Attempts to find the `id` of the given data set by `externalId` and returns the `id` if the `externalId` exists.

**Example**
    
    
    select dataset_id("EXAMPLE_DATASET") as dataSetId  
    

### cdf_assetSubtree​

  * **cdf_assetSubtree(externalId: String or id: BigInt): Table[Asset]**



Returns an asset subtree under a specific asset in an asset hierarchy, that is, all the child assets for a specific asset in an asset hierarchy are returned.

important

If the total size of subtree exceeds 100,000 assets, an error will be returned.

**Example**
    
    
    select * from cdf_assetSubtree('externalId of an asset')  
    select * from cdf_assetSubtree('id of an asset')  
    

### cdf_nodes​

  * **cdf_nodes(space of the view: String, externalId of the view: String, version of the view: String): Table[Nodes]**
  * **cdf_nodes(): Table[Nodes]**



Returns nodes in the CDF project as a table.

  * `cdf_nodes()` returns `space` and `externalId` of all nodes in the CDF project.
  * `cdf_nodes("space of the view: String", "externalId of the view: String"," version of the view: String")` returns a table with nodes ingested with `view` as reference.   
The table contains `space` and `externalId` columns and columns for each property in the `view`.



**Example**
    
    
    select * from cdf_nodes('space of the view: String', 'externalId of the view: String', 'version of the view: String')  
    select * from cdf_nodes()  
    

### cdf_edges​

  * **cdf_edges("space of the view: String", "externalId of the view: String", "version of the view: String"): Table[Edges]**
  * **cdf_edges(): Table[Edges]**



Returns edges in the CDF project as a table.

  * `cdf_edges()` returns `space`, `externalId`, `startNode`, `endNode`, and `type` of all edges in a CDF project.

  * `cdf_edges(space of the view: String, externalId of the view: String, version of the view: String)` returns a table with edges ingested with `view` as reference.   
The table contains `space`, `externalId`, `startNode`, `endNode`, and `type` columns and columns for each property in the `view`.




**Example**
    
    
    select * from cdf_edges('space of the view: String', 'externalId of the view: String', 'version of the view: String')  
    select * from cdf_edges()  
    

### node_reference​

  * **node_reference("space: String", "externalId: String"): STRUCT <"space:string", "externalId:string">**
  * **node_reference("externalId: String"): STRUCT <"space:String", "externalId:String">**



To reference a `node`, you need the _space_ `externalId` of the node and the _node_ `externalId`. Typically, you reference a node when writing or filtering _edges_ based on `startNode` and `endNode`.

`node_reference` accepts the single parameter `externalId` of the node. The target/instance space set at the transformation is used as the _space_ `externalId` of the node.

tip

`node_reference` will return `NULL` if it receives a `NULL` in the externalId parameter, this makes it easier to write to nullable fields.

important

If you're using `node_reference` for filtering i.e. in your `where` clause, you must add the _space_ `externalId` and the _node_ `externalId`.

**Example**
    
    
    select node_reference('space externalId of a node', 'externalId of a node') as startNode, node_reference('space externalId of a node', 'externalId of a node') as endNode, ... from mydb.mytable  
    select node_reference('externalId of a node') as startNode, node_reference('externalId of a node') as endNode, ... from mydb.mytable  
    select * from cdf_edges('space of the view: String', 'externalId of the view: String', 'version of the view: String') where startNode = node_reference('space externalId of a node', 'externalId of a node') or node_reference('space externalId of a node', 'externalId of a node')  
    

### type_reference​

  * **type_reference("space: String", "externalId: String"): STRUCT <"space:String", "externalId:String">**
  * **type_reference("externalId: String"): STRUCT <"space:String", "externalId:String">**



All edges have `type`. To filter edges based on `type`, use `type_reference` and provide the _space_ `externalId` and the _edge type_ `externalId`. If you're writing edges with a `view` reference, you must specify the edge type using `type_reference`.

`type_reference` accepts the single parameter `externalId` of the edge type. The target/instance space set at the transformation is used as the _space_ `externalId` of the edge type.

tip

`type_reference` will return `NULL` if it receives a `NULL` in the externalId parameter, this makes it easier to write to the nullable `_type` column of node instances.

important

If you're using `type_reference` for filtering i.e. in your `where` clause, you must add the _space_ `externalId` and the _edge type_ `externalId`.

**Example**
    
    
    select node_reference('space externalId of a node', 'externalId of a node') as startNode, type_reference('space externalId of a node', 'externalId of a node') as endNode, ... from mydb.mytable  
    select * from cdf_edges('space of the view: String', 'externalId of the view: String', 'version of the view: String') where type = type_reference('space externalId of a node', 'externalId of a node') or type_reference('space externalId of a node', 'externalId of a node')  
    select * from cdf_edges() where type = type_reference('space externalId of a node', 'externalId of a node') or type_reference('space externalId of a node', 'externalId of a node')  
    

### cdf_data_models​

  * **cdf_data_models("data model space: String", "data model externalId: String", "data model version: String", "type external id: String" ): Table[Nodes]**
  * **cdf_data_models("data model space: String", "data model externalId: String", "data model version: String", "type external id: String", "property in type containing the relationship: String" ): Table[Edges]**



These functions follow the data model UI lingo and make it easy to retrieve the data written to `types` and `relationship`.

To retrieve data from a `type` in your data model, provide the data model's `space`, `externalId`, `version` and the `externalId` of the type as input parameters to `cdf_data_models`.

To retrieve data from a `relationship` in your data model, provide the data model's `space`, `externalId`, `version`,the `externalId` of the `type` containing the relationship and the name of the relationship `property` in the `type` as input parameters to `cdf_data_models`.

**Example**
    
    
    select * from cdf_data_models('data model space: String', 'data model externalId: String', 'data model version: String', 'type external id: String')  
    select * from cdf_data_models('data model space: String', 'data model externalId: String', 'data model version: String', 'type external id: String', 'property in type where relationship is defined: String')  
    

### try_get_unit​

  * **try_get_unit("unit alias: String", "quantity: String"): String**
  * **try_get_unit("unit alias: String"): String**



This function allows the user to get a unit's `externalId` as defined by the [Cognite unit catalog](https://developer.cognite.com/dev/concepts/resource_types/units/) based on an alias and an optional quantity. Each unit in the catalog is associated with a quantity and a list of alias names. For instance, degrees Celsius has externalId `temperature:deg_c`, is of quantity `temperature`, and has a list of alias names that includes `deg_c`, `ºC` and `Celsius`.

Inside a `quantity`, the `unit alias` is unique. If the `unit alias` doesn't exist for the `quantity`, the function returns `null`.

If the `quantity` isn't specified, the function will only return a value if the `unit alias` is unique across all quantities. Otherwise, the function will return `null`.

important

If the `quantity` is not specified, the addition of an `unit alias` to the unit catalog could change the behavior of a call to this function by making the `unit alias` ambiguous. We therefore recommend to specify the `quantity` whenever possible to avoid ambiguities.

**Example**
    
    
    try_get_unit('Celsius', 'Temperature')  
    try_get_unit('C', 'Temperature')  
    try_get_unit('Celsius')  
    

These calls will all return `temperature:deg_c`.

### convert_unit​

  * **convert_unit("value: Number", "source unit external id: String", "target unit external id: String"): Double**
  * **convert_unit("value: Number", "source unit alias: String", "target unit alias: String", "quantity: String"): Double**
  * **convert_unit("value: Number", "source unit alias: String", "target unit alias: String"): Double**



This function allows the user to convert a `value` between units of the same quantity.

If the `value` is `null`, the function will return `null`.

The _source_ and _target_ units to convert between can be specified using the `externalId` or `unit alias` of each unit.

The `quantity` can also be specified to verify that the alias and external IDs refer to the right quantity. The function will return an error if the quantity and the aliases don't match.

In that case, the method could fail if there is no unit with such `unit alias`.

When using aliases without specifying the `quantity`, there could be ambiguous aliases. In these cases, the method will try to resolve the ambiguity by using aliases which have a `quantity` in common, therefore eliminating the ambiguity whenever possible.

If the `externalId` or `unit alias` don't have a `quantity` in common, it's impossible to convert the value between them. Therefore, the conversion will fail.

If the units don't exist, the conversion will fail.

**Example**
    
    
    convert_unit(10.0, 'temperature:deg_f', 'temperature:deg_c')  
    convert_unit(10, 'C', 'F', 'Temperature')  
    convert_unit(10, 'C', 'F')  
    

These calls will all return `50.0`.

Notice in the last example that "F" is an ambiguous alias as it could refer to either Fahrenheit degrees or Farad. In this case, the convert_unit method will automatically select Fahrenheit degrees because it is a unit of the `quantity` temperature and so are Celsius degrees. Therefore, the method will succeed and convert between Celsius degrees and Fahrenheit degrees as expected.

## Disabled Spark SQL functions​

We currently don't support using these Spark SQL functions when you transform data:

`xpath`

`xpath_boolean`

`xpath_double`

`xpath_float`

`xpath_int`

`xpath_number`

`xpath_short`

`xpath_string`

`xpath_long`

`java_method`

`reflect`

Last updated: July 10, 2025

  * Read from a CDF staging table
    * Avoid schema inference
  * Read from a CDF file
    * Avoid schema inference
  * Read from other CDF resource types
  * Load data incrementally
    * Resource types supporting incremental data loading on the `lastUpdatedTime` column
    * Incremental data loading when using Data Modeling
  * Backfill
  * Write to specific properties in data modeling
  * Custom SQL functions
    * get_names
    * cast_to_strings
    * to_metadata
    * to_metadata_except
    * asset_ids
    * is_new
    * dataset_id
    * cdf_assetSubtree
    * cdf_nodes
    * cdf_edges
    * node_reference
    * type_reference
    * cdf_data_models
    * try_get_unit
    * convert_unit
  * Disabled Spark SQL functions



E-learning

  * [Cognite Academy](https://learn.cognite.com/)



Community

  * [Cognite Hub](https://hub.cognite.com/)



Support

  * [Cognite Support](https://cognite.zendesk.com/hc/en-us)



Legal

  * [Terms and conditions](https://www.cognite.com/en/generalterms)



![](/images/logos/cogfooter.svg)![](/images/logos/cogfooter.svg)
