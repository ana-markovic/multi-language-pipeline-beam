package apache.beam.transformers;

import apache.beam.configuration.IPipelineOptions;
import org.apache.beam.runners.core.construction.External;
import org.apache.beam.sdk.transforms.*;
import org.apache.beam.sdk.values.PCollection;
import org.apache.beam.sdk.values.PDone;


import java.util.Arrays;
import java.util.List;

public class CrossLanguageTransform extends PTransform<PCollection<String>, PCollection<String>> {


    private static final String URN = "beam:transforms:xlang:pythontransform";

    private static String expansionAddress;

    public CrossLanguageTransform(String expansionAddress) {
        this.expansionAddress = expansionAddress;
    }

    @Override
    public PCollection<String> expand(PCollection<String> input) {
        return input.apply(
                        "ExternalPythonTransform",
                        External.of(URN, new byte[]{}, this.expansionAddress)
                );
    }
}
