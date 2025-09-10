# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a CDF (Cognite Data Fusion) bootcamp project using the Cognite Toolkit for data operations. The project focuses on ice cream factory data processing and OEE (Overall Equipment Effectiveness) calculations.

## Package Management

This project uses Rye for Python package management:
- `rye sync` - Install/update dependencies
- `rye lock` - Update lock files
- Dependencies are managed via `pyproject.toml`
- Lock files: `requirements.lock` and `requirements-dev.lock`

## Development Commands

### Testing Connectivity
- `python src/connection_test.py` - Test access to required external services and APIs

### CDF Operations
- Uses `cognite-toolkit` (version 0.6.19) as primary dependency
- Configuration in `cdf.toml`:
  - Default organization: `ice-cream-dataops`
  - Default environment: `test`
  - Modules version: `0.6.19`

## Architecture

### Directory Structure
- `src/cdf_bootcamp/` - Main Python package with simple hello() function
- `src/connection_test.py` - Connectivity testing utility
- `ice-cream-dataops/` - CDF toolkit modules and functions
  - `modules/bootcamp/` - Bootcamp-specific modules
    - `ice_cream_api/` - Ice cream factory API data extraction
    - `use_cases/oee/` - OEE calculation functions

### Key Components

#### Ice Cream API Data Extractor (`ice-cream-dataops/modules/bootcamp/ice_cream_api/functions/icapi_datapoints_extractor/`)
- Extracts datapoints from Ice Cream Factory API
- Handles multiple sites: Houston, Oslo, Kuala_Lumpur, Hannover, Nuremberg, Marseille, Sao_Paulo, Chicago, Rotterdam, London
- Uses CogniteAsset and CogniteTimeSeries from CDM v1
- Supports backfill and configurable time windows (max 336 hours)
- Implements extraction pipeline reporting
- Entry point: `handler.py:handle()`

#### OEE Time Series Calculator (`ice-cream-dataops/modules/bootcamp/use_cases/oee/functions/oee_timeseries/`)
- Calculates Overall Equipment Effectiveness metrics
- Processes: quality, performance, availability, and overall OEE
- Uses concurrent processing with ThreadPoolExecutor
- Creates missing time series automatically
- Handles data alignment and gap filling
- Entry point: `handler.py:handle()`

### Data Model Spaces
- `icapi_dm_space` - Source data from Ice Cream Factory API
- `oee_ts_space` - Calculated OEE time series data
- `cdf_cdm` - Cognite Core Data Model space

### External Dependencies
- Ice Cream Factory API: `https://ice-cream-factory.inso-internal.cognite.ai`
- Uses Cognite SDK for CDF operations
- NumPy and Pandas for data processing

## Important Notes
- Both extraction functions implement error handling and status reporting
- Time series filtering focuses on "planned_status" and "good" metrics
- OEE calculations require aligned datapoints across multiple time series
- Project uses CDM v1 (Cognite Core Data Model) for data modeling