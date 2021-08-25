package my.beam.transforms;

import org.apache.beam.sdk.transforms.*;
import org.apache.beam.sdk.values.KV;
import org.apache.beam.sdk.values.PCollection;

public class JavaExtractWords extends PTransform<PCollection<String>, PCollection<KV<String, Long>>> {

    final String prefix;

    public JavaExtractWords(String prefix) {
        this.prefix = prefix;
    }

    @Override
    public PCollection<KV<String, Long>> expand (PCollection<String> input){
        return input.apply("CountWords", Count.<String>perElement());
    }
}
