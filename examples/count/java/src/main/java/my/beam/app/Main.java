package apache.beam.app;

import apache.beam.configuration.IPipelineOptions;
import apache.beam.transformers.CrossLanguageTransform;
import apache.beam.transformers.PrintFn;
import org.apache.beam.sdk.Pipeline;
import org.apache.beam.sdk.coders.AvroGenericCoder;
import org.apache.beam.sdk.io.TextIO;
import org.apache.beam.sdk.options.PipelineOptions;
import org.apache.beam.sdk.options.PipelineOptionsFactory;
import org.apache.beam.sdk.transforms.*;
import org.apache.beam.sdk.values.KV;
import org.apache.beam.sdk.values.PCollection;

import java.util.Arrays;
import java.util.List;

public class Main {

    public static void main(String[] args) {
        Pipeline p = Pipeline.create();

        String expansionAddress = "localhost:9097";

        PCollection<String> input = p.apply(TextIO.read().from("gs://apache-beam-samples/shakespeare/*"));
        input.apply(new CrossLanguageTransform(expansionAddress)).apply(TextIO.write().to("wordcounts"));

        p.run().waitUntilFinish();
    }
}





