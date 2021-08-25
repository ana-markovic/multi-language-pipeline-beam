package apache.beam.transformers;

import org.apache.beam.sdk.transforms.DoFn;

public class PrintFn<T> extends DoFn<T, T> {
    @ProcessElement
    public void processElement(@Element T element, OutputReceiver<T> out) {
        System.out.println("JAVA OUTPUT: " + element);
        //out.output(element);
    }
}
