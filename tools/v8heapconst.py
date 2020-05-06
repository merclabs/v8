# Copyright 2019 the V8 project authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can
# be found in the LICENSE file.

# This file is automatically generated by mkgrokdump and should not
# be modified manually.

# List of known V8 instance types.
INSTANCE_TYPES = {
  0: "INTERNALIZED_STRING_TYPE",
  2: "EXTERNAL_INTERNALIZED_STRING_TYPE",
  8: "ONE_BYTE_INTERNALIZED_STRING_TYPE",
  10: "EXTERNAL_ONE_BYTE_INTERNALIZED_STRING_TYPE",
  18: "UNCACHED_EXTERNAL_INTERNALIZED_STRING_TYPE",
  26: "UNCACHED_EXTERNAL_ONE_BYTE_INTERNALIZED_STRING_TYPE",
  32: "STRING_TYPE",
  33: "CONS_STRING_TYPE",
  34: "EXTERNAL_STRING_TYPE",
  35: "SLICED_STRING_TYPE",
  37: "THIN_STRING_TYPE",
  40: "ONE_BYTE_STRING_TYPE",
  41: "CONS_ONE_BYTE_STRING_TYPE",
  42: "EXTERNAL_ONE_BYTE_STRING_TYPE",
  43: "SLICED_ONE_BYTE_STRING_TYPE",
  45: "THIN_ONE_BYTE_STRING_TYPE",
  50: "UNCACHED_EXTERNAL_STRING_TYPE",
  58: "UNCACHED_EXTERNAL_ONE_BYTE_STRING_TYPE",
  64: "SYMBOL_TYPE",
  65: "BIG_INT_BASE_TYPE",
  66: "HEAP_NUMBER_TYPE",
  67: "ODDBALL_TYPE",
  68: "ABSTRACT_INTERNAL_CLASS_SUBCLASS1_TYPE",
  69: "ABSTRACT_INTERNAL_CLASS_SUBCLASS2_TYPE",
  70: "FOREIGN_TYPE",
  71: "PROMISE_FULFILL_REACTION_JOB_TASK_TYPE",
  72: "PROMISE_REJECT_REACTION_JOB_TASK_TYPE",
  73: "CALLABLE_TASK_TYPE",
  74: "CALLBACK_TASK_TYPE",
  75: "PROMISE_RESOLVE_THENABLE_JOB_TASK_TYPE",
  76: "LOAD_HANDLER_TYPE",
  77: "STORE_HANDLER_TYPE",
  78: "FUNCTION_TEMPLATE_INFO_TYPE",
  79: "OBJECT_TEMPLATE_INFO_TYPE",
  80: "ACCESS_CHECK_INFO_TYPE",
  81: "ACCESSOR_INFO_TYPE",
  82: "ACCESSOR_PAIR_TYPE",
  83: "ALIASED_ARGUMENTS_ENTRY_TYPE",
  84: "ALLOCATION_MEMENTO_TYPE",
  85: "ALLOCATION_SITE_TYPE",
  86: "ARRAY_BOILERPLATE_DESCRIPTION_TYPE",
  87: "ASM_WASM_DATA_TYPE",
  88: "ASYNC_GENERATOR_REQUEST_TYPE",
  89: "BREAK_POINT_TYPE",
  90: "BREAK_POINT_INFO_TYPE",
  91: "CACHED_TEMPLATE_OBJECT_TYPE",
  92: "CALL_HANDLER_INFO_TYPE",
  93: "CLASS_POSITIONS_TYPE",
  94: "DEBUG_INFO_TYPE",
  95: "ENUM_CACHE_TYPE",
  96: "FEEDBACK_CELL_TYPE",
  97: "FUNCTION_TEMPLATE_RARE_DATA_TYPE",
  98: "INTERCEPTOR_INFO_TYPE",
  99: "INTERPRETER_DATA_TYPE",
  100: "PROMISE_CAPABILITY_TYPE",
  101: "PROMISE_REACTION_TYPE",
  102: "PROPERTY_DESCRIPTOR_OBJECT_TYPE",
  103: "PROTOTYPE_INFO_TYPE",
  104: "SCRIPT_TYPE",
  105: "SOURCE_TEXT_MODULE_INFO_ENTRY_TYPE",
  106: "STACK_FRAME_INFO_TYPE",
  107: "STACK_TRACE_FRAME_TYPE",
  108: "TEMPLATE_OBJECT_DESCRIPTION_TYPE",
  109: "TUPLE2_TYPE",
  110: "WASM_CAPI_FUNCTION_DATA_TYPE",
  111: "WASM_DEBUG_INFO_TYPE",
  112: "WASM_EXCEPTION_TAG_TYPE",
  113: "WASM_EXPORTED_FUNCTION_DATA_TYPE",
  114: "WASM_INDIRECT_FUNCTION_TABLE_TYPE",
  115: "WASM_JS_FUNCTION_DATA_TYPE",
  116: "WASM_VALUE_TYPE",
  117: "FIXED_ARRAY_TYPE",
  118: "HASH_TABLE_TYPE",
  119: "EPHEMERON_HASH_TABLE_TYPE",
  120: "GLOBAL_DICTIONARY_TYPE",
  121: "NAME_DICTIONARY_TYPE",
  122: "NUMBER_DICTIONARY_TYPE",
  123: "ORDERED_HASH_MAP_TYPE",
  124: "ORDERED_HASH_SET_TYPE",
  125: "ORDERED_NAME_DICTIONARY_TYPE",
  126: "SIMPLE_NUMBER_DICTIONARY_TYPE",
  127: "STRING_TABLE_TYPE",
  128: "CLOSURE_FEEDBACK_CELL_ARRAY_TYPE",
  129: "OBJECT_BOILERPLATE_DESCRIPTION_TYPE",
  130: "SCOPE_INFO_TYPE",
  131: "SCRIPT_CONTEXT_TABLE_TYPE",
  132: "BYTE_ARRAY_TYPE",
  133: "BYTECODE_ARRAY_TYPE",
  134: "FIXED_DOUBLE_ARRAY_TYPE",
  135: "INTERNAL_CLASS_WITH_SMI_ELEMENTS_TYPE",
  136: "AWAIT_CONTEXT_TYPE",
  137: "BLOCK_CONTEXT_TYPE",
  138: "CATCH_CONTEXT_TYPE",
  139: "DEBUG_EVALUATE_CONTEXT_TYPE",
  140: "EVAL_CONTEXT_TYPE",
  141: "FUNCTION_CONTEXT_TYPE",
  142: "MODULE_CONTEXT_TYPE",
  143: "NATIVE_CONTEXT_TYPE",
  144: "SCRIPT_CONTEXT_TYPE",
  145: "WITH_CONTEXT_TYPE",
  146: "SMALL_ORDERED_HASH_MAP_TYPE",
  147: "SMALL_ORDERED_HASH_SET_TYPE",
  148: "SMALL_ORDERED_NAME_DICTIONARY_TYPE",
  149: "EXPORTED_SUB_CLASS_BASE_TYPE",
  150: "EXPORTED_SUB_CLASS_TYPE",
  151: "SOURCE_TEXT_MODULE_TYPE",
  152: "SYNTHETIC_MODULE_TYPE",
  153: "UNCOMPILED_DATA_WITH_PREPARSE_DATA_TYPE",
  154: "UNCOMPILED_DATA_WITHOUT_PREPARSE_DATA_TYPE",
  155: "WEAK_FIXED_ARRAY_TYPE",
  156: "TRANSITION_ARRAY_TYPE",
  157: "CELL_TYPE",
  158: "CODE_TYPE",
  159: "CODE_DATA_CONTAINER_TYPE",
  160: "COVERAGE_INFO_TYPE",
  161: "DESCRIPTOR_ARRAY_TYPE",
  162: "EMBEDDER_DATA_ARRAY_TYPE",
  163: "FEEDBACK_METADATA_TYPE",
  164: "FEEDBACK_VECTOR_TYPE",
  165: "FILLER_TYPE",
  166: "FREE_SPACE_TYPE",
  167: "INTERNAL_CLASS_TYPE",
  168: "INTERNAL_CLASS_WITH_STRUCT_ELEMENTS_TYPE",
  169: "MAP_TYPE",
  170: "PREPARSE_DATA_TYPE",
  171: "PROPERTY_ARRAY_TYPE",
  172: "PROPERTY_CELL_TYPE",
  173: "SHARED_FUNCTION_INFO_TYPE",
  174: "SMI_BOX_TYPE",
  175: "SMI_PAIR_TYPE",
  176: "SORT_STATE_TYPE",
  177: "WASM_STRUCT_TYPE",
  178: "WEAK_ARRAY_LIST_TYPE",
  179: "WEAK_CELL_TYPE",
  180: "JS_PROXY_TYPE",
  1057: "JS_OBJECT_TYPE",
  181: "JS_GLOBAL_OBJECT_TYPE",
  182: "JS_GLOBAL_PROXY_TYPE",
  183: "JS_MODULE_NAMESPACE_TYPE",
  1040: "JS_SPECIAL_API_OBJECT_TYPE",
  1041: "JS_PRIMITIVE_WRAPPER_TYPE",
  1042: "JS_MAP_KEY_ITERATOR_TYPE",
  1043: "JS_MAP_KEY_VALUE_ITERATOR_TYPE",
  1044: "JS_MAP_VALUE_ITERATOR_TYPE",
  1045: "JS_SET_KEY_VALUE_ITERATOR_TYPE",
  1046: "JS_SET_VALUE_ITERATOR_TYPE",
  1047: "JS_GENERATOR_OBJECT_TYPE",
  1048: "JS_ASYNC_FUNCTION_OBJECT_TYPE",
  1049: "JS_ASYNC_GENERATOR_OBJECT_TYPE",
  1050: "JS_DATA_VIEW_TYPE",
  1051: "JS_TYPED_ARRAY_TYPE",
  1052: "JS_MAP_TYPE",
  1053: "JS_SET_TYPE",
  1054: "JS_WEAK_MAP_TYPE",
  1055: "JS_WEAK_SET_TYPE",
  1056: "JS_API_OBJECT_TYPE",
  1058: "JS_AGGREGATE_ERROR_TYPE",
  1059: "JS_ARGUMENTS_OBJECT_TYPE",
  1060: "JS_ARRAY_TYPE",
  1061: "JS_ARRAY_BUFFER_TYPE",
  1062: "JS_ARRAY_ITERATOR_TYPE",
  1063: "JS_ASYNC_FROM_SYNC_ITERATOR_TYPE",
  1064: "JS_COLLATOR_TYPE",
  1065: "JS_CONTEXT_EXTENSION_OBJECT_TYPE",
  1066: "JS_DATE_TYPE",
  1067: "JS_DATE_TIME_FORMAT_TYPE",
  1068: "JS_DISPLAY_NAMES_TYPE",
  1069: "JS_ERROR_TYPE",
  1070: "JS_FINALIZATION_REGISTRY_TYPE",
  1071: "JS_LIST_FORMAT_TYPE",
  1072: "JS_LOCALE_TYPE",
  1073: "JS_MESSAGE_OBJECT_TYPE",
  1074: "JS_NUMBER_FORMAT_TYPE",
  1075: "JS_PLURAL_RULES_TYPE",
  1076: "JS_PROMISE_TYPE",
  1077: "JS_REG_EXP_TYPE",
  1078: "JS_REG_EXP_STRING_ITERATOR_TYPE",
  1079: "JS_RELATIVE_TIME_FORMAT_TYPE",
  1080: "JS_SEGMENT_ITERATOR_TYPE",
  1081: "JS_SEGMENTER_TYPE",
  1082: "JS_STRING_ITERATOR_TYPE",
  1083: "JS_V8_BREAK_ITERATOR_TYPE",
  1084: "JS_WEAK_REF_TYPE",
  1085: "WASM_EXCEPTION_OBJECT_TYPE",
  1086: "WASM_GLOBAL_OBJECT_TYPE",
  1087: "WASM_INSTANCE_OBJECT_TYPE",
  1088: "WASM_MEMORY_OBJECT_TYPE",
  1089: "WASM_MODULE_OBJECT_TYPE",
  1090: "WASM_TABLE_OBJECT_TYPE",
  1091: "JS_BOUND_FUNCTION_TYPE",
  1092: "JS_FUNCTION_TYPE",
}

# List of known V8 maps.
KNOWN_MAPS = {
  ("read_only_space", 0x00121): (166, "FreeSpaceMap"),
  ("read_only_space", 0x00149): (169, "MetaMap"),
  ("read_only_space", 0x0018d): (67, "NullMap"),
  ("read_only_space", 0x001c5): (161, "DescriptorArrayMap"),
  ("read_only_space", 0x001f5): (155, "WeakFixedArrayMap"),
  ("read_only_space", 0x0021d): (165, "OnePointerFillerMap"),
  ("read_only_space", 0x00245): (165, "TwoPointerFillerMap"),
  ("read_only_space", 0x00289): (67, "UninitializedMap"),
  ("read_only_space", 0x002cd): (8, "OneByteInternalizedStringMap"),
  ("read_only_space", 0x00329): (67, "UndefinedMap"),
  ("read_only_space", 0x0035d): (66, "HeapNumberMap"),
  ("read_only_space", 0x003a1): (67, "TheHoleMap"),
  ("read_only_space", 0x00401): (67, "BooleanMap"),
  ("read_only_space", 0x00489): (132, "ByteArrayMap"),
  ("read_only_space", 0x004b1): (117, "FixedArrayMap"),
  ("read_only_space", 0x004d9): (117, "FixedCOWArrayMap"),
  ("read_only_space", 0x00501): (118, "HashTableMap"),
  ("read_only_space", 0x00529): (64, "SymbolMap"),
  ("read_only_space", 0x00551): (40, "OneByteStringMap"),
  ("read_only_space", 0x00579): (130, "ScopeInfoMap"),
  ("read_only_space", 0x005a1): (173, "SharedFunctionInfoMap"),
  ("read_only_space", 0x005c9): (158, "CodeMap"),
  ("read_only_space", 0x005f1): (157, "CellMap"),
  ("read_only_space", 0x00619): (172, "GlobalPropertyCellMap"),
  ("read_only_space", 0x00641): (70, "ForeignMap"),
  ("read_only_space", 0x00669): (156, "TransitionArrayMap"),
  ("read_only_space", 0x00691): (45, "ThinOneByteStringMap"),
  ("read_only_space", 0x006b9): (164, "FeedbackVectorMap"),
  ("read_only_space", 0x0070d): (67, "ArgumentsMarkerMap"),
  ("read_only_space", 0x0076d): (67, "ExceptionMap"),
  ("read_only_space", 0x007c9): (67, "TerminationExceptionMap"),
  ("read_only_space", 0x00831): (67, "OptimizedOutMap"),
  ("read_only_space", 0x00891): (67, "StaleRegisterMap"),
  ("read_only_space", 0x008d5): (131, "ScriptContextTableMap"),
  ("read_only_space", 0x008fd): (128, "ClosureFeedbackCellArrayMap"),
  ("read_only_space", 0x00925): (163, "FeedbackMetadataArrayMap"),
  ("read_only_space", 0x0094d): (117, "ArrayListMap"),
  ("read_only_space", 0x00975): (65, "BigIntMap"),
  ("read_only_space", 0x0099d): (129, "ObjectBoilerplateDescriptionMap"),
  ("read_only_space", 0x009c5): (133, "BytecodeArrayMap"),
  ("read_only_space", 0x009ed): (159, "CodeDataContainerMap"),
  ("read_only_space", 0x00a15): (160, "CoverageInfoMap"),
  ("read_only_space", 0x00a3d): (134, "FixedDoubleArrayMap"),
  ("read_only_space", 0x00a65): (120, "GlobalDictionaryMap"),
  ("read_only_space", 0x00a8d): (96, "ManyClosuresCellMap"),
  ("read_only_space", 0x00ab5): (117, "ModuleInfoMap"),
  ("read_only_space", 0x00add): (121, "NameDictionaryMap"),
  ("read_only_space", 0x00b05): (96, "NoClosuresCellMap"),
  ("read_only_space", 0x00b2d): (122, "NumberDictionaryMap"),
  ("read_only_space", 0x00b55): (96, "OneClosureCellMap"),
  ("read_only_space", 0x00b7d): (123, "OrderedHashMapMap"),
  ("read_only_space", 0x00ba5): (124, "OrderedHashSetMap"),
  ("read_only_space", 0x00bcd): (125, "OrderedNameDictionaryMap"),
  ("read_only_space", 0x00bf5): (170, "PreparseDataMap"),
  ("read_only_space", 0x00c1d): (171, "PropertyArrayMap"),
  ("read_only_space", 0x00c45): (92, "SideEffectCallHandlerInfoMap"),
  ("read_only_space", 0x00c6d): (92, "SideEffectFreeCallHandlerInfoMap"),
  ("read_only_space", 0x00c95): (92, "NextCallSideEffectFreeCallHandlerInfoMap"),
  ("read_only_space", 0x00cbd): (126, "SimpleNumberDictionaryMap"),
  ("read_only_space", 0x00ce5): (117, "SloppyArgumentsElementsMap"),
  ("read_only_space", 0x00d0d): (146, "SmallOrderedHashMapMap"),
  ("read_only_space", 0x00d35): (147, "SmallOrderedHashSetMap"),
  ("read_only_space", 0x00d5d): (148, "SmallOrderedNameDictionaryMap"),
  ("read_only_space", 0x00d85): (151, "SourceTextModuleMap"),
  ("read_only_space", 0x00dad): (127, "StringTableMap"),
  ("read_only_space", 0x00dd5): (152, "SyntheticModuleMap"),
  ("read_only_space", 0x00dfd): (154, "UncompiledDataWithoutPreparseDataMap"),
  ("read_only_space", 0x00e25): (153, "UncompiledDataWithPreparseDataMap"),
  ("read_only_space", 0x00e4d): (178, "WeakArrayListMap"),
  ("read_only_space", 0x00e75): (119, "EphemeronHashTableMap"),
  ("read_only_space", 0x00e9d): (162, "EmbedderDataArrayMap"),
  ("read_only_space", 0x00ec5): (179, "WeakCellMap"),
  ("read_only_space", 0x00eed): (32, "StringMap"),
  ("read_only_space", 0x00f15): (41, "ConsOneByteStringMap"),
  ("read_only_space", 0x00f3d): (33, "ConsStringMap"),
  ("read_only_space", 0x00f65): (37, "ThinStringMap"),
  ("read_only_space", 0x00f8d): (35, "SlicedStringMap"),
  ("read_only_space", 0x00fb5): (43, "SlicedOneByteStringMap"),
  ("read_only_space", 0x00fdd): (34, "ExternalStringMap"),
  ("read_only_space", 0x01005): (42, "ExternalOneByteStringMap"),
  ("read_only_space", 0x0102d): (50, "UncachedExternalStringMap"),
  ("read_only_space", 0x01055): (0, "InternalizedStringMap"),
  ("read_only_space", 0x0107d): (2, "ExternalInternalizedStringMap"),
  ("read_only_space", 0x010a5): (10, "ExternalOneByteInternalizedStringMap"),
  ("read_only_space", 0x010cd): (18, "UncachedExternalInternalizedStringMap"),
  ("read_only_space", 0x010f5): (26, "UncachedExternalOneByteInternalizedStringMap"),
  ("read_only_space", 0x0111d): (58, "UncachedExternalOneByteStringMap"),
  ("read_only_space", 0x01145): (67, "SelfReferenceMarkerMap"),
  ("read_only_space", 0x01179): (95, "EnumCacheMap"),
  ("read_only_space", 0x011c9): (86, "ArrayBoilerplateDescriptionMap"),
  ("read_only_space", 0x012c5): (98, "InterceptorInfoMap"),
  ("read_only_space", 0x03335): (71, "PromiseFulfillReactionJobTaskMap"),
  ("read_only_space", 0x0335d): (72, "PromiseRejectReactionJobTaskMap"),
  ("read_only_space", 0x03385): (73, "CallableTaskMap"),
  ("read_only_space", 0x033ad): (74, "CallbackTaskMap"),
  ("read_only_space", 0x033d5): (75, "PromiseResolveThenableJobTaskMap"),
  ("read_only_space", 0x033fd): (78, "FunctionTemplateInfoMap"),
  ("read_only_space", 0x03425): (79, "ObjectTemplateInfoMap"),
  ("read_only_space", 0x0344d): (80, "AccessCheckInfoMap"),
  ("read_only_space", 0x03475): (81, "AccessorInfoMap"),
  ("read_only_space", 0x0349d): (82, "AccessorPairMap"),
  ("read_only_space", 0x034c5): (83, "AliasedArgumentsEntryMap"),
  ("read_only_space", 0x034ed): (84, "AllocationMementoMap"),
  ("read_only_space", 0x03515): (87, "AsmWasmDataMap"),
  ("read_only_space", 0x0353d): (88, "AsyncGeneratorRequestMap"),
  ("read_only_space", 0x03565): (89, "BreakPointMap"),
  ("read_only_space", 0x0358d): (90, "BreakPointInfoMap"),
  ("read_only_space", 0x035b5): (91, "CachedTemplateObjectMap"),
  ("read_only_space", 0x035dd): (93, "ClassPositionsMap"),
  ("read_only_space", 0x03605): (94, "DebugInfoMap"),
  ("read_only_space", 0x0362d): (97, "FunctionTemplateRareDataMap"),
  ("read_only_space", 0x03655): (99, "InterpreterDataMap"),
  ("read_only_space", 0x0367d): (100, "PromiseCapabilityMap"),
  ("read_only_space", 0x036a5): (101, "PromiseReactionMap"),
  ("read_only_space", 0x036cd): (102, "PropertyDescriptorObjectMap"),
  ("read_only_space", 0x036f5): (103, "PrototypeInfoMap"),
  ("read_only_space", 0x0371d): (104, "ScriptMap"),
  ("read_only_space", 0x03745): (105, "SourceTextModuleInfoEntryMap"),
  ("read_only_space", 0x0376d): (106, "StackFrameInfoMap"),
  ("read_only_space", 0x03795): (107, "StackTraceFrameMap"),
  ("read_only_space", 0x037bd): (108, "TemplateObjectDescriptionMap"),
  ("read_only_space", 0x037e5): (109, "Tuple2Map"),
  ("read_only_space", 0x0380d): (110, "WasmCapiFunctionDataMap"),
  ("read_only_space", 0x03835): (111, "WasmDebugInfoMap"),
  ("read_only_space", 0x0385d): (112, "WasmExceptionTagMap"),
  ("read_only_space", 0x03885): (113, "WasmExportedFunctionDataMap"),
  ("read_only_space", 0x038ad): (114, "WasmIndirectFunctionTableMap"),
  ("read_only_space", 0x038d5): (115, "WasmJSFunctionDataMap"),
  ("read_only_space", 0x038fd): (116, "WasmValueMap"),
  ("read_only_space", 0x03925): (167, "InternalClassMap"),
  ("read_only_space", 0x0394d): (175, "SmiPairMap"),
  ("read_only_space", 0x03975): (174, "SmiBoxMap"),
  ("read_only_space", 0x0399d): (149, "ExportedSubClassBaseMap"),
  ("read_only_space", 0x039c5): (150, "ExportedSubClassMap"),
  ("read_only_space", 0x039ed): (68, "AbstractInternalClassSubclass1Map"),
  ("read_only_space", 0x03a15): (69, "AbstractInternalClassSubclass2Map"),
  ("read_only_space", 0x03a3d): (135, "InternalClassWithSmiElementsMap"),
  ("read_only_space", 0x03a65): (168, "InternalClassWithStructElementsMap"),
  ("read_only_space", 0x03a8d): (176, "SortStateMap"),
  ("read_only_space", 0x03ab5): (85, "AllocationSiteWithWeakNextMap"),
  ("read_only_space", 0x03add): (85, "AllocationSiteWithoutWeakNextMap"),
  ("read_only_space", 0x03b05): (76, "LoadHandler1Map"),
  ("read_only_space", 0x03b2d): (76, "LoadHandler2Map"),
  ("read_only_space", 0x03b55): (76, "LoadHandler3Map"),
  ("read_only_space", 0x03b7d): (77, "StoreHandler0Map"),
  ("read_only_space", 0x03ba5): (77, "StoreHandler1Map"),
  ("read_only_space", 0x03bcd): (77, "StoreHandler2Map"),
  ("read_only_space", 0x03bf5): (77, "StoreHandler3Map"),
  ("map_space", 0x00121): (1057, "ExternalMap"),
  ("map_space", 0x00149): (1073, "JSMessageObjectMap"),
}

# List of known V8 objects.
KNOWN_OBJECTS = {
  ("read_only_space", 0x00171): "NullValue",
  ("read_only_space", 0x001b5): "EmptyDescriptorArray",
  ("read_only_space", 0x001ed): "EmptyWeakFixedArray",
  ("read_only_space", 0x0026d): "UninitializedValue",
  ("read_only_space", 0x0030d): "UndefinedValue",
  ("read_only_space", 0x00351): "NanValue",
  ("read_only_space", 0x00385): "TheHoleValue",
  ("read_only_space", 0x003d9): "HoleNanValue",
  ("read_only_space", 0x003e5): "TrueValue",
  ("read_only_space", 0x0044d): "FalseValue",
  ("read_only_space", 0x0047d): "empty_string",
  ("read_only_space", 0x006e1): "EmptyScopeInfo",
  ("read_only_space", 0x006e9): "EmptyFixedArray",
  ("read_only_space", 0x006f1): "ArgumentsMarker",
  ("read_only_space", 0x00751): "Exception",
  ("read_only_space", 0x007ad): "TerminationException",
  ("read_only_space", 0x00815): "OptimizedOut",
  ("read_only_space", 0x00875): "StaleRegister",
  ("read_only_space", 0x0116d): "EmptyEnumCache",
  ("read_only_space", 0x011a1): "EmptyPropertyArray",
  ("read_only_space", 0x011a9): "EmptyByteArray",
  ("read_only_space", 0x011b1): "EmptyObjectBoilerplateDescription",
  ("read_only_space", 0x011bd): "EmptyArrayBoilerplateDescription",
  ("read_only_space", 0x011f1): "EmptyClosureFeedbackCellArray",
  ("read_only_space", 0x011f9): "EmptySloppyArgumentsElements",
  ("read_only_space", 0x01209): "EmptySlowElementDictionary",
  ("read_only_space", 0x0122d): "EmptyOrderedHashMap",
  ("read_only_space", 0x01241): "EmptyOrderedHashSet",
  ("read_only_space", 0x01255): "EmptyFeedbackMetadata",
  ("read_only_space", 0x01261): "EmptyPropertyCell",
  ("read_only_space", 0x01275): "EmptyPropertyDictionary",
  ("read_only_space", 0x0129d): "NoOpInterceptorInfo",
  ("read_only_space", 0x012ed): "EmptyWeakArrayList",
  ("read_only_space", 0x012f9): "InfinityValue",
  ("read_only_space", 0x01305): "MinusZeroValue",
  ("read_only_space", 0x01311): "MinusInfinityValue",
  ("read_only_space", 0x0131d): "SelfReferenceMarker",
  ("read_only_space", 0x0135d): "OffHeapTrampolineRelocationInfo",
  ("read_only_space", 0x01369): "TrampolineTrivialCodeDataContainer",
  ("read_only_space", 0x01375): "TrampolinePromiseRejectionCodeDataContainer",
  ("read_only_space", 0x01381): "GlobalThisBindingScopeInfo",
  ("read_only_space", 0x013b9): "EmptyFunctionScopeInfo",
  ("read_only_space", 0x013e1): "NativeScopeInfo",
  ("read_only_space", 0x013fd): "HashSeed",
  ("old_space", 0x00121): "ArgumentsIteratorAccessor",
  ("old_space", 0x00165): "ArrayLengthAccessor",
  ("old_space", 0x001a9): "BoundFunctionLengthAccessor",
  ("old_space", 0x001ed): "BoundFunctionNameAccessor",
  ("old_space", 0x00231): "ErrorStackAccessor",
  ("old_space", 0x00275): "FunctionArgumentsAccessor",
  ("old_space", 0x002b9): "FunctionCallerAccessor",
  ("old_space", 0x002fd): "FunctionNameAccessor",
  ("old_space", 0x00341): "FunctionLengthAccessor",
  ("old_space", 0x00385): "FunctionPrototypeAccessor",
  ("old_space", 0x003c9): "RegExpResultIndicesAccessor",
  ("old_space", 0x0040d): "StringLengthAccessor",
  ("old_space", 0x00451): "InvalidPrototypeValidityCell",
  ("old_space", 0x00459): "EmptyScript",
  ("old_space", 0x00499): "ManyClosuresCell",
  ("old_space", 0x004a5): "ArrayConstructorProtector",
  ("old_space", 0x004b9): "NoElementsProtector",
  ("old_space", 0x004cd): "IsConcatSpreadableProtector",
  ("old_space", 0x004e1): "ArraySpeciesProtector",
  ("old_space", 0x004f5): "TypedArraySpeciesProtector",
  ("old_space", 0x00509): "PromiseSpeciesProtector",
  ("old_space", 0x0051d): "RegExpSpeciesProtector",
  ("old_space", 0x00531): "StringLengthProtector",
  ("old_space", 0x00545): "ArrayIteratorProtector",
  ("old_space", 0x00559): "ArrayBufferDetachingProtector",
  ("old_space", 0x0056d): "PromiseHookProtector",
  ("old_space", 0x00581): "PromiseResolveProtector",
  ("old_space", 0x00595): "MapIteratorProtector",
  ("old_space", 0x005a9): "PromiseThenProtector",
  ("old_space", 0x005bd): "SetIteratorProtector",
  ("old_space", 0x005d1): "StringIteratorProtector",
  ("old_space", 0x005e5): "SingleCharacterStringCache",
  ("old_space", 0x009ed): "StringSplitCache",
  ("old_space", 0x00df5): "RegExpMultipleCache",
  ("old_space", 0x011fd): "BuiltinsConstantsTable",
  ("old_space", 0x015a1): "AsyncFunctionAwaitRejectSharedFun",
  ("old_space", 0x015c9): "AsyncFunctionAwaitResolveSharedFun",
  ("old_space", 0x015f1): "AsyncGeneratorAwaitRejectSharedFun",
  ("old_space", 0x01619): "AsyncGeneratorAwaitResolveSharedFun",
  ("old_space", 0x01641): "AsyncGeneratorYieldResolveSharedFun",
  ("old_space", 0x01669): "AsyncGeneratorReturnResolveSharedFun",
  ("old_space", 0x01691): "AsyncGeneratorReturnClosedRejectSharedFun",
  ("old_space", 0x016b9): "AsyncGeneratorReturnClosedResolveSharedFun",
  ("old_space", 0x016e1): "AsyncIteratorValueUnwrapSharedFun",
}

# Lower 32 bits of first page addresses for various heap spaces.
HEAP_FIRST_PAGES = {
  0x08100000: "old_space",
  0x08140000: "map_space",
  0x08040000: "read_only_space",
}

# List of known V8 Frame Markers.
FRAME_MARKERS = (
  "ENTRY",
  "CONSTRUCT_ENTRY",
  "EXIT",
  "OPTIMIZED",
  "WASM_COMPILED",
  "WASM_TO_JS",
  "JS_TO_WASM",
  "WASM_DEBUG_BREAK",
  "C_WASM_ENTRY",
  "WASM_EXIT",
  "WASM_COMPILE_LAZY",
  "INTERPRETED",
  "STUB",
  "BUILTIN_CONTINUATION",
  "JAVA_SCRIPT_BUILTIN_CONTINUATION",
  "JAVA_SCRIPT_BUILTIN_CONTINUATION_WITH_CATCH",
  "INTERNAL",
  "CONSTRUCT",
  "ARGUMENTS_ADAPTOR",
  "BUILTIN",
  "BUILTIN_EXIT",
  "NATIVE",
)

# This set of constants is generated from a shipping build.
