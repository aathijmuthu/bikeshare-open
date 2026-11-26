# Verification evidence

The agent executed these experiments using the assignment’s seeded-fault workflow; hook scripts were invoked directly.

## Test written before feature implementation

Command: `make test` (virtual environment on PATH). Exit 2.

```text
python -m pytest tests/ -q
...........F....                                                         [100%]
=================================== FAILURES ===================================
______________ test_rolling_std_uses_previous_seven_calendar_days ______________

self = Index(['instant', 'season', 'yr', 'mnth', 'holiday', 'weekday', 'temp',
       'atemp', 'hum', 'windspeed', 'casual', ...kday', 'month_sin', 'month_cos',
       'weather_severity', 'cnt_lag_1', 'cnt_lag_7', 'cnt_roll_7'],
      dtype='str')
key = 'cnt_std_7'

    def get_loc(self, key):
        """
        Get integer location, slice or boolean mask for requested label.
    
        Parameters
        ----------
        key : label
            The key to check its location if it is present in the index.
    
        Returns
        -------
        int if unique index, slice if monotonic index, else mask
            Integer location, slice or boolean mask.
    
        See Also
        --------
        Index.get_slice_bound : Calculate slice bound that corresponds to
            given label.
        Index.get_indexer : Computes indexer and mask for new index given
            the current index.
        Index.get_non_unique : Returns indexer and masks for new index given
            the current index.
        Index.get_indexer_for : Returns an indexer even when non-unique.
    
        Examples
        --------
        >>> unique_index = pd.Index(list("abc"))
        >>> unique_index.get_loc("b")
        1
    
        >>> monotonic_index = pd.Index(list("abbc"))
        >>> monotonic_index.get_loc("b")
        slice(1, 3, None)
    
        >>> non_monotonic_index = pd.Index(list("abcb"))
        >>> non_monotonic_index.get_loc("b")
        array([False,  True, False,  True])
        """
        casted_key = self._maybe_cast_indexer(key)
        try:
>           return self._engine.get_loc(casted_key)
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.venv/lib/python3.12/site-packages/pandas/core/indexes/base.py:3641: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
pandas/_libs/index.pyx:168: in pandas._libs.index.IndexEngine.get_loc
    ???
pandas/_libs/index.pyx:197: in pandas._libs.index.IndexEngine.get_loc
    ???
pandas/_libs/hashtable_class_helper.pxi:7668: in pandas._libs.hashtable.PyObjectHashTable.get_item
    ???
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

>   ???
E   KeyError: 'cnt_std_7'

pandas/_libs/hashtable_class_helper.pxi:7676: KeyError

The above exception was the direct cause of the following exception:

feats =         dteday  instant  season  ...  cnt_lag_1 cnt_lag_7   cnt_roll_7
0   2011-01-10     10.0  WINTER  ...      822.0...    1787.0  1530.142857
713 2012-12-31    731.0  WINTER  ...     1796.0     920.0  1531.428571

[714 rows x 28 columns]

    def test_rolling_std_uses_previous_seven_calendar_days(feats):
        """Demand volatility on 2012-02-15 uses February 8 through 14 only."""
        raw = load_raw().set_index('dteday')
        days = pd.date_range('2012-02-08', '2012-02-14')
        values = [float(raw.loc[d, TARGET]) for d in days]
        mean = sum(values) / 7
        expected = (sum((v - mean) ** 2 for v in values) / 7) ** 0.5
>       actual = feats.set_index('dteday').loc[pd.Timestamp('2012-02-15'), 'cnt_std_7']
                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

tests/test_leakage.py:76: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
.venv/lib/python3.12/site-packages/pandas/core/indexing.py:1199: in __getitem__
    return self.obj._get_value(*key, takeable=self._takeable)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.12/site-packages/pandas/core/frame.py:4489: in _get_value
    series = self._get_item(col)
             ^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.12/site-packages/pandas/core/frame.py:4969: in _get_item
    loc = self.columns.get_loc(item)
          ^^^^^^^^^^^^^^^^^^^^^^^^^^
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = Index(['instant', 'season', 'yr', 'mnth', 'holiday', 'weekday', 'temp',
       'atemp', 'hum', 'windspeed', 'casual', ...kday', 'month_sin', 'month_cos',
       'weather_severity', 'cnt_lag_1', 'cnt_lag_7', 'cnt_roll_7'],
      dtype='str')
key = 'cnt_std_7'

    def get_loc(self, key):
        """
        Get integer location, slice or boolean mask for requested label.
    
        Parameters
        ----------
        key : label
            The key to check its location if it is present in the index.
    
        Returns
        -------
        int if unique index, slice if monotonic index, else mask
            Integer location, slice or boolean mask.
    
        See Also
        --------
        Index.get_slice_bound : Calculate slice bound that corresponds to
            given label.
        Index.get_indexer : Computes indexer and mask for new index given
            the current index.
        Index.get_non_unique : Returns indexer and masks for new index given
            the current index.
        Index.get_indexer_for : Returns an indexer even when non-unique.
    
        Examples
        --------
        >>> unique_index = pd.Index(list("abc"))
        >>> unique_index.get_loc("b")
        1
    
        >>> monotonic_index = pd.Index(list("abbc"))
        >>> monotonic_index.get_loc("b")
        slice(1, 3, None)
    
        >>> non_monotonic_index = pd.Index(list("abcb"))
        >>> non_monotonic_index.get_loc("b")
        array([False,  True, False,  True])
        """
        casted_key = self._maybe_cast_indexer(key)
        try:
            return self._engine.get_loc(casted_key)
        except KeyError as err:
            if isinstance(casted_key, slice) or (
                isinstance(casted_key, abc.Iterable)
                and any(isinstance(x, slice) for x in casted_key)
            ):
                raise InvalidIndexError(key) from err
>           raise KeyError(key) from err
E           KeyError: 'cnt_std_7'

.venv/lib/python3.12/site-packages/pandas/core/indexes/base.py:3648: KeyError
=========================== short test summary info ============================
FAILED tests/test_leakage.py::test_rolling_std_uses_previous_seven_calendar_days
1 failed, 15 passed in 44.91s
make: *** [test] Error 1

```

## forbidden

Exact temporary diff:
```diff
diff --git a/src/features.py b/src/features.py
index 8b5d5d8..66d645e 100644
--- a/src/features.py
+++ b/src/features.py
@@ -83,7 +83,7 @@ def build_features(df: pd.DataFrame) -> pd.DataFrame:
 def feature_columns(df: pd.DataFrame) -> list[str]:
     """Numeric columns that are safe to feed the model."""
     numeric = df.select_dtypes(include="number").columns
-    return [c for c in numeric if c not in FORBIDDEN]
+    return [c for c in numeric if c not in FORBIDDEN or c == "registered"]
 
 
 if __name__ == "__main__":

```
Full test output (exit 2):
```text
python -m pytest tests/ -q
.......F..........                                                       [100%]
=================================== FAILURES ===================================
__________________________ test_no_forbidden_features __________________________

feats =         dteday  instant  season  ...  cnt_lag_7   cnt_roll_7    cnt_std_7
0   2011-01-10     10.0  WINTER  ...     134....142857   820.919420
713 2012-12-31    731.0  WINTER  ...      920.0  1531.428571   821.327646

[714 rows x 29 columns]

    def test_no_forbidden_features(feats):
        """Guards the gate, not the data: feature_columns() excludes FORBIDDEN by
        construction, so this cannot discover a *new* leaky column. What it
        catches is someone editing feature_columns() or FORBIDDEN -- which is
        exactly the fault the Step 7 hook demonstrates."""
        cols = set(feature_columns(feats))
>       assert not (cols & FORBIDDEN), f"forbidden columns in feature set: {cols & FORBIDDEN}"
E       AssertionError: forbidden columns in feature set: {'registered'}
E       assert not ({'atemp', 'cnt_lag_1', 'cnt_lag_7', 'cnt_roll_7', 'cnt_std_7', 'dayofweek', ...} & {'casual', 'cnt', 'cnt_2d_bfr', 'days_since_2011', 'instant', 'registered', ...})

tests/test_leakage.py:31: AssertionError
=========================== short test summary info ============================
FAILED tests/test_leakage.py::test_no_forbidden_features - AssertionError: fo...
1 failed, 17 passed in 1.23s
make: *** [test] Error 1

```
Direct hook invocation stderr (exit 2):
```text
Leakage tests failed after editing /Users/amuthu/Desktop/DSC 180A/bikeshare-open-starter/src/features.py:
feats =         dteday  instant  season  ...  cnt_lag_7   cnt_roll_7    cnt_std_7
0   2011-01-10     10.0  WINTER  ...     134....142857   820.919420
713 2012-12-31    731.0  WINTER  ...      920.0  1531.428571   821.327646

[714 rows x 29 columns]

    def test_no_forbidden_features(feats):
        """Guards the gate, not the data: feature_columns() excludes FORBIDDEN by
        construction, so this cannot discover a *new* leaky column. What it
        catches is someone editing feature_columns() or FORBIDDEN -- which is
        exactly the fault the Step 7 hook demonstrates."""
        cols = set(feature_columns(feats))
>       assert not (cols & FORBIDDEN), f"forbidden columns in feature set: {cols & FORBIDDEN}"
E       AssertionError: forbidden columns in feature set: {'registered'}
E       assert not ({'atemp', 'cnt_lag_1', 'cnt_lag_7', 'cnt_roll_7', 'cnt_std_7', 'dayofweek', ...} & {'casual', 'cnt', 'cnt_2d_bfr', 'days_since_2011', 'instant', 'registered', ...})

tests/test_leakage.py:31: AssertionError
=========================== short test summary info ============================
FAILED tests/test_leakage.py::test_no_forbidden_features - AssertionError: fo...
1 failed, 8 passed in 0.23s

```
Restoration output (exit 0):
```text
python -m pytest tests/ -q
..................                                                       [100%]
18 passed in 0.80s

```
Repair: one deterministic restoration in this execution. Interactive harness repair turns were not measured; hook dispatch remains untested.

## rolling

Exact temporary diff:
```diff
diff --git a/src/features.py b/src/features.py
index 8b5d5d8..0c4c017 100644
--- a/src/features.py
+++ b/src/features.py
@@ -73,7 +73,7 @@ def build_features(df: pd.DataFrame) -> pd.DataFrame:
     # If you add a longer lag, raise LAG_WARMUP in src/config.py.
     out["cnt_lag_1"] = out[TARGET].shift(1)
     out["cnt_lag_7"] = out[TARGET].shift(LAG_WARMUP)
-    out["cnt_roll_7"] = out[TARGET].shift(1).rolling(LAG_WARMUP).mean()
+    out["cnt_roll_7"] = out[TARGET].rolling(LAG_WARMUP).mean()
 
     out["cnt_std_7"] = out[TARGET].shift(1).rolling(LAG_WARMUP).std(ddof=0)
 

```
Full test output (exit 2):
```text
python -m pytest tests/ -q
..........F.......                                                       [100%]
=================================== FAILURES ===================================
_______________________ test_rolling_mean_excludes_today _______________________

feats =         dteday  instant  season  ...  cnt_lag_7   cnt_roll_7    cnt_std_7
0   2011-01-10     10.0  WINTER  ...     134....428571   820.919420
713 2012-12-31    731.0  WINTER  ...      920.0  1789.857143   821.327646

[714 rows x 29 columns]

    def test_rolling_mean_excludes_today(feats):
        """cnt_roll_7 must be the mean of the 7 calendar days *before* today."""
        by_date = feats.set_index("dteday")[TARGET]
        date = feats.dteday.iloc[200]
        window = [date - pd.Timedelta(days=k) for k in range(1, 8)]
        if all(d in by_date.index for d in window):
            expected = sum(by_date[d] for d in window) / 7
>           assert feats.set_index("dteday").cnt_roll_7[date] == pytest.approx(expected)
E           assert np.float64(4389.0) == 4414.857142857143 ± 0.00441486
E             
E             comparison failed
E             Obtained: 4389.0
E             Expected: 4414.857142857143 ± 0.00441486

tests/test_leakage.py:57: AssertionError
=========================== short test summary info ============================
FAILED tests/test_leakage.py::test_rolling_mean_excludes_today - assert np.fl...
1 failed, 17 passed in 0.90s
make: *** [test] Error 1

```
Direct hook invocation stderr (exit 2):
```text
Leakage tests failed after editing /Users/amuthu/Desktop/DSC 180A/bikeshare-open-starter/src/features.py:
[714 rows x 29 columns]

    def test_rolling_mean_excludes_today(feats):
        """cnt_roll_7 must be the mean of the 7 calendar days *before* today."""
        by_date = feats.set_index("dteday")[TARGET]
        date = feats.dteday.iloc[200]
        window = [date - pd.Timedelta(days=k) for k in range(1, 8)]
        if all(d in by_date.index for d in window):
            expected = sum(by_date[d] for d in window) / 7
>           assert feats.set_index("dteday").cnt_roll_7[date] == pytest.approx(expected)
E           assert np.float64(4389.0) == 4414.857142857143 ± 0.00441486
E             
E             comparison failed
E             Obtained: 4389.0
E             Expected: 4414.857142857143 ± 0.00441486

tests/test_leakage.py:57: AssertionError
=========================== short test summary info ============================
FAILED tests/test_leakage.py::test_rolling_mean_excludes_today - assert np.fl...
1 failed, 8 passed in 0.24s

```
Restoration output (exit 0):
```text
python -m pytest tests/ -q
..................                                                       [100%]
18 passed in 0.82s

```
Repair: one deterministic restoration in this execution. Interactive harness repair turns were not measured; hook dispatch remains untested.

## weather

Exact temporary diff:
```diff
diff --git a/src/features.py b/src/features.py
index 8b5d5d8..03f6e5c 100644
--- a/src/features.py
+++ b/src/features.py
@@ -27,7 +27,7 @@ def encode_weather(series: pd.Series) -> pd.Series:
     known = series.dropna()
     unknown = set(known.unique()) - set(WEATHER_ORDER)
     if unknown:
-        raise ValueError(f"unmapped weather labels: {sorted(unknown)}")
+        pass # seeded fault: silently map unknown weather to NaN
     return series.map(WEATHER_ORDER).astype(float)
 
 

```
Full test output (exit 2):
```text
python -m pytest tests/ -q
..............F...                                                       [100%]
=================================== FAILURES ===================================
_______________________ test_unknown_weather_is_rejected _______________________

    def test_unknown_weather_is_rejected():
        from src.features import encode_weather
>       with pytest.raises(ValueError, match='unmapped weather'):
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
E       Failed: DID NOT RAISE ValueError

tests/test_leakage.py:82: Failed
=========================== short test summary info ============================
FAILED tests/test_leakage.py::test_unknown_weather_is_rejected - Failed: DID ...
1 failed, 17 passed in 0.91s
make: *** [test] Error 1

```
Direct hook invocation stderr (exit 2):
```text
Leakage tests failed after editing /Users/amuthu/Desktop/DSC 180A/bikeshare-open-starter/src/features.py:
........F                                                                [100%]
=================================== FAILURES ===================================
_______________________ test_unknown_weather_is_rejected _______________________

    def test_unknown_weather_is_rejected():
        from src.features import encode_weather
>       with pytest.raises(ValueError, match='unmapped weather'):
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
E       Failed: DID NOT RAISE ValueError

tests/test_leakage.py:82: Failed
=========================== short test summary info ============================
FAILED tests/test_leakage.py::test_unknown_weather_is_rejected - Failed: DID ...
1 failed, 8 passed in 0.24s

```
Restoration output (exit 0):
```text
python -m pytest tests/ -q
..................                                                       [100%]
18 passed in 0.80s

```
Repair: one deterministic restoration in this execution. Interactive harness repair turns were not measured; hook dispatch remains untested.

## Bash copy bypass (isolated disposable copy)

The actual submission CSV was never modified. To respect its immutability, this experiment ran against a temporary copy of src/, data/raw/, and .claude/. The replacement changes the first count from 1349 to 1350. The same hook payload lacks file_path, so the hook exits without testing. Claude Code permission dispatch was not exercised.

```text
$ cp /var/folders/gz/6kb8kdpj15v5wds8xxrn24rm0000gn/T/bikeshare-fault-r2lk67v7/replacement.csv /var/folders/gz/6kb8kdpj15v5wds8xxrn24rm0000gn/T/bikeshare-fault-r2lk67v7/data/raw/bike_daily.csv
exit 0
stdout: ''
stderr: ''
$ bash .claude/hooks/check_leakage.sh < Bash-payload.json
exit 0
stdout: ''
stderr: ''
$ make data
python -m src.ingest
Traceback (most recent call last):
  File "<frozen runpy>", line 198, in _run_module_as_main
  File "<frozen runpy>", line 88, in _run_code
  File "/private/var/folders/gz/6kb8kdpj15v5wds8xxrn24rm0000gn/T/bikeshare-fault-r2lk67v7/src/ingest.py", line 39, in <module>
    df = load_raw()
         ^^^^^^^^^^
  File "/private/var/folders/gz/6kb8kdpj15v5wds8xxrn24rm0000gn/T/bikeshare-fault-r2lk67v7/src/ingest.py", line 27, in load_raw
    raise ValueError(f"raw data SHA-256 mismatch: {digest}; restore the immutable starter CSV")
ValueError: raw data SHA-256 mismatch: 0f24d32bc1244c85a4f57a93369ef362ff3833d27456c8f475645cc404272c50; restore the immutable starter CSV
make: *** [data] Error 1
exit 2
```

Implemented protection: load_raw verifies the starter SHA-256 before parsing, so make data and every consumer reject a changed CSV. A PreToolUse Bash policy or filesystem write protection could prevent the copy itself; a PostToolUse Edit/Write hook cannot.
