from src.util.check_functions import (
    check_arguments,
    check_metric_value,
    check_metric_values,
    check_number_of_files,
)
from src.util.get_functions import (
    get_files_data_frame,
    get_test_root_dir,
)
from src.core.measures_functions import (
    calculate_em1,
    calculate_em2,
    calculate_em3,
    calculate_em4,
    calculate_em5,
    calculate_em6,
    calculate_em7,
    calculate_em8
)

import pandas as pd


def non_complex_files_density(data_frame):
    """
    Calculates non-complex files density (em1).
    This function calculates non-complex files density measure (em1)
    used to assess the changeability quality subcharacteristic.

    This function gets the dataframe metrics
    and returns the non-complex files density measure (em1).
    """
    check_arguments(data_frame)
    files_df = get_files_data_frame(data_frame)

    files_complexity = files_df["complexity"].astype(float)  # m1 metric
    files_functions = files_df["functions"].astype(float)  # m2 metric
    number_of_files = len(files_df)  # Tm3 metric

    check_number_of_files(number_of_files)
    check_metric_values(files_complexity, "complexity")
    check_metric_values(files_functions, "functions")

    return calculate_em1(data={
        "complexity": files_complexity,
        "functions": files_functions,
        "number_of_files": number_of_files,
    })


def commented_files_density(data_frame: pd.DataFrame):
    """
    Calculates commented files density (em2).

    This function gets the dataframe metrics
    and returns the commented files density measure (em2).
    """
    check_arguments(data_frame)
    files_df = get_files_data_frame(data_frame)

    number_of_files = len(files_df)  # Tm3 metric
    files_comment_lines_density = files_df["comment_lines_density"].astype(float)  # m4 metric

    check_number_of_files(number_of_files)
    check_metric_values(files_comment_lines_density, "comment_lines_density")

    return calculate_em2(data={
        "number_of_files": number_of_files,
        "comment_lines_density": files_comment_lines_density,
    })


def absence_of_duplications(data_frame: pd.DataFrame):
    """
    Calculates duplicated files absence (em3).

    This function gets the dataframe metrics
    and returns the duplicated files absence measure (em3).
    """
    check_arguments(data_frame)
    files_df = get_files_data_frame(data_frame)

    files_duplicated_lines_density = files_df["duplicated_lines_density"].astype(float)  # m5 metric
    number_of_files = len(files_df)  # Tm3 metric

    check_number_of_files(number_of_files)
    check_metric_values(files_duplicated_lines_density, "duplicated_lines_density")

    return calculate_em3(data={
        "number_of_files": number_of_files,
        "duplicated_lines_density": files_duplicated_lines_density,
    })


def test_coverage(data_frame):
    """
    Calculates test coverage (em6).

    This function gets the dataframe metrics
    and returns the test coverage measure (em6).
    """
    check_arguments(data_frame)
    files_df = get_files_data_frame(data_frame)

    number_of_files = len(files_df)  # m3 metric
    coverage = files_df["coverage"].astype(float)  # m6 metric

    check_number_of_files(number_of_files)
    check_metric_values(coverage, "coverage")

    return calculate_em6(data={
        "coverage": coverage,
        "number_of_files": number_of_files,
    })


def fast_test_builds(data_frame):
    """
    Calculates fast test builds (em5)
    This function gets the dataframe metrics
    and returns the fast test builds measure (em5).
    """
    root_test = get_test_root_dir(data_frame)

    check_metric_value(root_test["test_execution_time"], "test_execution_time")

    test_execution_time = float(root_test["test_execution_time"])  # m9 metric

    return calculate_em5(data={
        "test_execution_time": test_execution_time
    })


def passed_tests(data_frame):
    """
    Calculates passed tests (em4)

    This function gets the dataframe metrics
    and returns the passed tests measure (em4).
    """
    root_test = get_test_root_dir(data_frame)

    check_metric_value(root_test["tests"], "tests")
    check_metric_value(root_test["test_errors"], "test_errors")
    check_metric_value(root_test["test_failures"], "test_failures")

    tests = float(root_test["tests"])  # m6 metrics
    test_errors = float(root_test["test_errors"])  # m7 metrics
    test_failures = float(root_test["test_failures"])  # m8 metrics

    return calculate_em4(data={
        "tests": tests,
        "test_errors": test_errors,
        "test_failures": test_failures,
    })


def team_throughput(data_frame):
    """
    Calculates team throughput (em7)

    This function gets the dataframe metrics
    and returns the team throughput measure.
    """
    check_arguments(data_frame)

    number_of_resolved_issues = int(data_frame["number_of_resolved_issues_in_the_last_7_days"])  # m10 metrics
    total_number_of_issues = int(data_frame["total_number_of_issues_in_the_last_7_days"])  # m11 metrics

    check_metric_value(number_of_resolved_issues, "number_of_resolved_issues")
    check_metric_value(total_number_of_issues, "total_number_of_issues")

    return calculate_em7(data={
        "number_of_resolved_issues": number_of_resolved_issues,
        "total_number_of_issues": total_number_of_issues,
    })


def ci_feedback_time(data_frame):
    """
    Calculates CI feedback time measure (em8)

    This function calculates average feedback time from CI system.
    """

    root_test = get_test_root_dir(data_frame)

    number_of_build_pipelines_in_the_last_x_days = root_test[number_of_build_pipelines_in_the_last_x_days]
    runtime_sum_of_build_pipelines_in_the_last_x_days = root_test[runtime_sum_of_build_pipelines_in_the_last_x_days]

    check_metric_value(
        number_of_build_pipelines_in_the_last_x_days,
        "number_of_build_pipelines_in_the_last_x_days",
    )

    check_metric_value(
        runtime_sum_of_build_pipelines_in_the_last_x_days,
        "runtime_sum_of_build_pipelines_in_the_last_x_days",
    )

    data = {
        "number_of_build_pipelines_in_the_last_x_days":
            number_of_build_pipelines_in_the_last_x_days,

        "runtime_sum_of_build_pipelines_in_the_last_x_days":
            runtime_sum_of_build_pipelines_in_the_last_x_days
    }

    return calculate_em8(data)
